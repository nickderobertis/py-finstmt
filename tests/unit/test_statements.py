from finstmt import FinancialStatements


def test_series_name(annual_capiq_stmts: FinancialStatements):
    stmts = annual_capiq_stmts

    # Check Investory Name is set
    assert stmts.inventory.name == "Inventory"
    # Check Cash & Cash Equivalents Name is set. This item includes spaces and a special character.
    assert stmts.cash.name == "Cash & Cash Equivalents"
