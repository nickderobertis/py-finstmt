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


