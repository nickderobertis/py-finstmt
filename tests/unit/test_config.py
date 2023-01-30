from finstmt import BalanceSheets, FinancialStatements, IncomeStatements


def test_config_attribute_access(
    annual_capiq_income_stmt: IncomeStatements, annual_capiq_bs_stmt: BalanceSheets
):
    dates = annual_capiq_income_stmt.dates
    stmts = FinancialStatements(annual_capiq_income_stmt, annual_capiq_bs_stmt[dates])
    # Check reading a config value by attribute access
    assert stmts.config.cash.display_name == "Cash and Cash Equivalents"

    # Check updating a config value by attribute access
    stmts.config.cash.display_name = "Cash"
    assert stmts.config.cash.display_name == "Cash"
    assert "cash" in dir(stmts.config)
