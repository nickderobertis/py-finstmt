

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
            display_name="equity",
            expr_str="cash[t]",
        ),
    ]
    dict = {
        "12/31/2022": {
            "cash": 1000,
        }
    }

    stmt_timeseries = FinStatementsBase.from_dict(
        dict,
        "Test Statment",
        config
    )
    finstmts = FinancialStatements([stmt_timeseries])
    assert finstmts.equity[0] == 1000

