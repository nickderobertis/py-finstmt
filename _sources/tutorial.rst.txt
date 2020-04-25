Getting started with finstmt
**********************************

Install
=======

Install via::

    pip install finstmt

Usage
=========

This is a simple example to construct financial statements::

    bs_path = r'WMT Balance Sheet.xlsx'
    inc_path = r'WMT Income Statement.xlsx'
    bs_df = pd.read_excel(bs_path)
    inc_df = pd.read_excel(inc_path)
    bs_data = BalanceSheets.from_df(bs_df)
    inc_data = IncomeStatements.from_df(inc_df)
    stmts = FinancialStatements(inc_data, bs_data)




Forecasting
=============

See the example notebook for an example of forecasting. The available forecast
methods are:

- ``auto``: Uses ``fbprophet``
- ``trend``: Fits a linear trend regression
- ``cagr``: Calculates the compounded annual growth rate (CAGR) and grows each future period at that rate
- ``mean``: Uses an average of the historical to predict the future
- ``recent``: Uses the most recent value to predict the future