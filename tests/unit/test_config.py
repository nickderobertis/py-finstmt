from finstmt import FinancialStatements


def test_config_attribute_access(ro_annual_capiq_stmts: FinancialStatements):
    stmts = ro_annual_capiq_stmts

    # Check reading a config value by attribute access
    assert stmts.config.cash.display_name == "Cash and Cash Equivalents"

    # Check updating a config value by attribute access
    stmts.config.cash.display_name = "Cash"
    assert stmts.config.cash.display_name == "Cash"
    assert "cash" in dir(stmts.config)
