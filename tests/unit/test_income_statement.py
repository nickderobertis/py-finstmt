from finstmt import FinancialStatements


def test_ebitda(ro_annual_capiq_stmts: FinancialStatements):
    stmts = ro_annual_capiq_stmts

    # Check that EBITDA = EBIT + DA
    assert (
        stmts.income_statements.ebitda
        == stmts.income_statements.ebit + stmts.income_statements.dep_exp
    ).all()
