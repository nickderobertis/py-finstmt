from finstmt.combined.statements import FinancialStatements
from finstmt.findata.statementsbase import FinStatementsBase
from finstmt.items.config import ItemConfig


def test_calculated_field():
    config = [
        ItemConfig(
            key="cash",
            display_name="Cash",
            extract_names=["cash"],
        ),
        ItemConfig(
            key="equity",
            display_name="Equity",
            expr_str="cash[t]",
        ),
    ]
    dict = {
        "12/31/2022": {
            "cash": 1000,
        }
    }

    stmt_timeseries = FinStatementsBase.from_dict(dict, "Test Statment", config)
    finstmts = FinancialStatements([stmt_timeseries])
    assert finstmts.equity[0] == 1000


def test_nested_calculated_fields():
    config = [
        ItemConfig(
            key="cash",
            display_name="Cash",
            extract_names=["cash"],
        ),
        ItemConfig(
            key="assets",
            display_name="Assets",
            expr_str="cash[t]",
        ),
        ItemConfig(
            key="equity",
            display_name="Equity",
            expr_str="assets[t]",
        ),
    ]
    dict = {
        "12/31/2022": {
            "cash": 1000,
        }
    }

    stmt_timeseries = FinStatementsBase.from_dict(dict, "Test Statment", config)
    finstmts = FinancialStatements([stmt_timeseries])
    assert finstmts.equity[0] == 1000


# Equity is defined BEFORE Assets in config file where assets and equity are a calculated field
def test_nested_calculated_fields_out_of_order():
    config = [
        ItemConfig(
            key="cash",
            display_name="Cash",
            extract_names=["cash"],
        ),
        ItemConfig(
            key="equity",
            display_name="Equity",
            expr_str="assets[t]",
        ),
        ItemConfig(
            key="assets",
            display_name="Assets",
            expr_str="cash[t]",
        ),
    ]
    dict = {
        "12/31/2022": {
            "cash": 1000,
        }
    }

    stmt_timeseries = FinStatementsBase.from_dict(dict, "Test Statment", config)
    finstmts = FinancialStatements([stmt_timeseries])
    assert finstmts.equity[0] == 1000
