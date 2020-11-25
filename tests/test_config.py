import json
from pathlib import Path

from finstmt import FinancialStatements, IncomeStatements, BalanceSheets
from finstmt.config_manage.statements import StatementsConfigManager
from tests.conftest import DEVELOPMENT_MODE, EXPECT_CONFIG_PATH


def check_config(config: StatementsConfigManager, json_path: Path):
    if DEVELOPMENT_MODE:
        json_data = config.json(indent=2)
        json_path.write_text(json_data)
        return

    expect_data = json.loads(json_path.read_text())
    assert config.dict() == expect_data


def test_config_load(annual_stockrow_income_stmt_cat: IncomeStatements, annual_stockrow_bs_stmt_cat: BalanceSheets):
    stmts = FinancialStatements(annual_stockrow_income_stmt_cat, annual_stockrow_bs_stmt_cat)
    json_path = EXPECT_CONFIG_PATH / 'default-cat-annual-stockrow.json'
    check_config(stmts.config, json_path)

