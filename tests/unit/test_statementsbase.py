from finstmt.findata.statementsbase import FinStatementsBase
from finstmt.items.config import ItemConfig


def test_load_from_dict():
    config = [
        ItemConfig(
            key="cash",
            display_name="Cash",
            extract_names=["cash"],
        )
    ]
    dict = {
        "12/31/2022": {
            "cash": 1000,
        }
    }

    stmt = FinStatementsBase.from_dict(dict, "Test Statment", config)

    assert stmt.cash[0] == 1000
