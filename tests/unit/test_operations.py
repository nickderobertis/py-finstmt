from finstmt import FinancialStatements
from finstmt.forecast.statements import ForecastedFinancialStatements


def test_round_statement(ro_annual_capiq_stmts: FinancialStatements):
    stmts = ro_annual_capiq_stmts

    rounded_whole = round(stmts)
    assert (rounded_whole.cash == round(stmts.cash)).all()

    rounded_decimal = round(stmts, 2)
    assert (rounded_decimal.cash == round(stmts.cash, 2)).all()


def test_round_forecasted_statements(
    ro_annual_capiq_fcst_stmts: ForecastedFinancialStatements,
):
    fcst = ro_annual_capiq_fcst_stmts

    rounded_whole = round(fcst)
    assert (rounded_whole.cash == round(fcst.cash)).all()
    assert (
        rounded_whole.forecasts["cash"].series == round(fcst.forecasts["cash"].series)
    ).all()
    assert rounded_whole.forecasts["cash"].item_config.manual_forecasts["levels"] == [
        round(val)
        for val in fcst.forecasts["cash"].item_config.manual_forecasts["levels"]
    ]

    rounded_decimal = round(fcst, 2)
    assert (rounded_decimal.cash == round(fcst.cash, 2)).all()
    assert (
        rounded_decimal.forecasts["cash"].series
        == round(fcst.forecasts["cash"].series, 2)
    ).all()
    assert rounded_decimal.forecasts["cash"].item_config.manual_forecasts["levels"] == [
        round(val, 2)
        for val in fcst.forecasts["cash"].item_config.manual_forecasts["levels"]
    ]


def test_add_statements(ro_annual_capiq_stmts: FinancialStatements):
    stmts = ro_annual_capiq_stmts

    added = stmts + stmts
    assert (added.cash == stmts.cash + stmts.cash).all()


def test_add_forecasted_statements_number(
    ro_annual_capiq_fcst_stmts: ForecastedFinancialStatements,
):
    fcst = ro_annual_capiq_fcst_stmts

    added = fcst + 1
    assert (added.cash == fcst.cash + 1).all()
    assert (added.forecasts["cash"].series == fcst.forecasts["cash"].series + 1).all()


def test_add_statements_number(ro_annual_capiq_stmts: FinancialStatements):
    stmts = ro_annual_capiq_stmts

    added = stmts + 1
    assert (added.cash == stmts.cash + 1).all()


def test_subtract_statements(ro_annual_capiq_stmts: FinancialStatements):
    stmts = ro_annual_capiq_stmts

    subtracted = stmts - stmts
    assert (subtracted.cash == stmts.cash - stmts.cash).all()


def test_subtract_statements_number(ro_annual_capiq_stmts: FinancialStatements):
    stmts = ro_annual_capiq_stmts

    subtracted = stmts - 1
    assert (subtracted.cash == stmts.cash - 1).all()


def test_multiply_statements(ro_annual_capiq_stmts: FinancialStatements):
    stmts = ro_annual_capiq_stmts

    multiplied = stmts * stmts
    assert (multiplied.cash == stmts.cash * stmts.cash).all()


def test_multiply_statements_number(ro_annual_capiq_stmts: FinancialStatements):
    stmts = ro_annual_capiq_stmts

    multiplied = stmts * 2
    assert (multiplied.cash == stmts.cash * 2).all()


def test_divide_statements(ro_annual_capiq_stmts: FinancialStatements):
    stmts = ro_annual_capiq_stmts

    divided = stmts / stmts
    assert (divided.cash == 1).all()


def test_divide_statements_number(ro_annual_capiq_stmts: FinancialStatements):
    stmts = ro_annual_capiq_stmts

    divided = stmts / 2
    assert (divided.cash == stmts.cash / 2).all()
