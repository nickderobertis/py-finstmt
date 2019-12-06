from finstmt import FinancialStatements, IncomeStatements, BalanceSheets


class TestLoadStockrow:

    def test_annual(self, annual_stockrow_income_df, annual_stockrow_bs_df):
        bs = BalanceSheets.from_df(annual_stockrow_bs_df)
        inc = IncomeStatements.from_df(annual_stockrow_income_df)
        stmts = FinancialStatements(inc, bs)

    def test_quarterly(self, quarterly_stockrow_income_df, quarterly_stockrow_bs_df):
        bs = BalanceSheets.from_df(quarterly_stockrow_bs_df)
        inc = IncomeStatements.from_df(quarterly_stockrow_income_df)
        stmts = FinancialStatements(inc, bs)

