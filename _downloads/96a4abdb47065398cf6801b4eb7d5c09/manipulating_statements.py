"""
Manipulating Statements
=======================

    Note: The formatting of the statements is off in the web view.
    Download the Jupyter notebook for the full experience.

First import the necessary classes and ``pandas``.

"""

import os
os.chdir('..')
from finstmt import FinancialStatements, IncomeStatements, BalanceSheets
import pandas as pd


######################################################################
# Load Financial Statements
# -------------------------
# 

root_folder = os.path.sep.join(['..', 'tests', 'sources', 'stockrow', 'CAT'])

inc_path = os.path.join(root_folder, 'annual_income.csv')
bs_path = os.path.join(root_folder, 'annual_bs.csv')

inc_df = pd.read_csv(inc_path, index_col=0)
bs_df = pd.read_csv(bs_path, index_col=0)

bs = BalanceSheets.from_df(bs_df)
inc = IncomeStatements.from_df(inc_df)
stmts = FinancialStatements(inc, bs)


######################################################################
# View Statements
# ---------------
# 

stmts


######################################################################
# Select Statement Periods
# ------------------------
# 
# Statements periods can be selected by indexing the statements object
# with them.
# 

stmts['12-31-2018']  # one period


######################################################################
# Now select multiple periods. Notice how the date format doesn't matter.
# 

stmts[['12/31/2015', '12-31-2018']]


######################################################################
# Statement Math
# --------------
# 
# All of the math operators are valid on statements. If the operation is
# with a number, it will apply to each item. If the operation is with
# another statement, for any overlapping time periods, it will apply the
# operation on the two items, while for non-overlapping time periods it
# will combine the statements.
# 
# Adjust Units
# ~~~~~~~~~~~~
# 
# It is easy to adjust units by multiplying or dividing the statements.
# 

stmts / 1000000  # in millions


######################################################################
# Math with Overlapping Statements
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
# If the time periods overlap, math will be done with each pair of items.
# This can be useful for aggregating statements from subsidiaries,
# segments, etc.:
# 

stmts + stmts


######################################################################
# Combine Non-Overlapping Statements
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
# If the statements have different time periods, adding them will put both
# sets of periods in a single statement.
# 

stmts['12/31/2018'] + stmts['12/31/2014']


######################################################################
# This can be very useful in the case where you have done a forecast and
# need to calculate something which requires data from the last historical
# period, such as FCF.
# 

stmts.config.update_all(['forecast_config', 'method'], 'trend')
fcst = stmts.forecast(periods=2)
(stmts[stmts.dates[-1]] + fcst).fcf.dropna()