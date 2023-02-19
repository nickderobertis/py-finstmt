from finstmt import FinancialStatements


def test_round_statement(annual_capiq_stmts: FinancialStatements):
    stmts = annual_capiq_stmts

    rounded_whole = round(stmts)
    assert (rounded_whole.cash == round(stmts.cash)).all()

    rounded_decimal = round(stmts, 2)
    assert (rounded_decimal.cash == round(stmts.cash, 2)).all()
