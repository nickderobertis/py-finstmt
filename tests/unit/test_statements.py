from finstmt import FinancialStatements


def test_series_name(ro_annual_capiq_stmts: FinancialStatements):
    stmts = ro_annual_capiq_stmts

    # Check Investory Name is set
    assert stmts.inventory.name == "Inventory"
    # Check Cash and Cash Equivalents Name is set. This item includes spaces
    assert stmts.cash.name == "Cash and Cash Equivalents"
    # Check a calculated item name is set
    # nwc is now a first class config item
    # TODO: Test a different calculated field if they will still exist
    # assert stmts.nwc.name == "nwc"
