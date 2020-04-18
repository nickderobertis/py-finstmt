"""
Forecasting Financial Statements with ``finstmt``
=================================================

    Note: The plots are not coming through and the formatting of the
    statements is off in the web view. Download the Jupyter notebook for
    the full experience.

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
# View Existing Statements
# ~~~~~~~~~~~~~~~~~~~~~~~~
# 

stmts


######################################################################
# Run a Forecast
# --------------
# 


######################################################################
# Set the Default Method
# ~~~~~~~~~~~~~~~~~~~~~~
# 
# This is not a necessary step, but this is the way to change the default
# forecast method. The default is already ``cagr`` and so this doesn't
# actually have an effect.
# 

stmts.config.update_all(['forecast_config', 'method'], 'cagr')


######################################################################
# Run the First Forecast
# ~~~~~~~~~~~~~~~~~~~~~~
# 
# Forecasts are run using ``.forecast()`` and produce
# ``ForecastedFinancialStatements``. It is usually good practice to first
# run a forecast, then view the results, then adjust as needed.
# 

fcst = stmts.forecast()


######################################################################
#     Note: Warnings are raised because CAGR is the default method but it
#     is not suitable for items which begin with 0
# 
# Now view the forecast.
# 

fcst


######################################################################
# And the plot:
# 

fcst.plot()


######################################################################
# It is also possible to plot a subset. Let's focus on only a few items
# for sake of example.
# 

fcst.plot(subset=['revenue', 'cogs', 'cash'])


######################################################################
# Change Methods and Re-Run Forecast
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
# After viewing the plots, the appropriate methods for forecasting each
# item should be chosen. Then they can be updated.
# 

stmts.config.update('cash', ['forecast_config', 'method'], 'trend')
stmts.config.update('cogs', ['forecast_config', 'method'], 'mean')


######################################################################
# Now re-run the forecast.
# 

fcst = stmts.forecast()


######################################################################
# And plot the results:
# 

fcst.plot(subset=['revenue', 'cogs', 'cash'])


######################################################################
# Now the methods for those forecasts has been updated.
# 
# Adjusting an Existing Forecast
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
# While it is possible to use the ``manual`` forecast type and pass in the
# desired growth rates or levels from the beginning, it is often more
# convenient to first run the forecast, then simply adjust it. The
# ``.to_manual`` method of the forecast was added for this purpose.
# 
# Either ``adjustments`` or ``replacements`` can be passed while updating,
# and either the level of the item or the growth in the item can be used
# for the new manual forecast.
# 

fcst.forecasts['cash'].to_manual(adjustments=[0, 0.4, 0, 0, 0])  # boost second forecast period cash growth by 40%
fcst.forecasts['revenue'].to_manual(use_levels=True, replacements={1: 8e10})  # set second forecast period revenue to 80,000,000,000


######################################################################
# The existing forecast is updated without running a new one. Now view the
# plots:
# 

fcst.plot(subset=['revenue', 'cogs', 'cash'])