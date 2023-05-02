import os

import pandas as pd
import pytest

from finstmt import FinancialStatements
from finstmt.findata.statementsbase import FinStatementsBase
from tests.fixtures.data.common import DATA_PATH
from finstmt.config.statement_config import BALANCE_SHEET_INPUT_CONFIG, INCOME_STATEMENT_CONFIG

STOCKROW_PATH = os.path.join(DATA_PATH, "stockrow")
CAT_PATH = os.path.join(STOCKROW_PATH, "CAT")


def annual_stockrow_income_df_cat() -> pd.DataFrame:
    annual_path = os.path.join(CAT_PATH, "annual_income.csv")
    df = pd.read_csv(annual_path, index_col=0)
    return df


@pytest.fixture
def annual_stockrow_income_stmt_cat() -> FinStatementsBase:
    stmt = FinStatementsBase.from_df(annual_stockrow_income_df_cat(), INCOME_STATEMENT_CONFIG.display_name, INCOME_STATEMENT_CONFIG.items_config_list)
    return stmt


def annual_stockrow_bs_df_cat() -> pd.DataFrame:
    annual_path = os.path.join(CAT_PATH, "annual_bs.csv")
    df = pd.read_csv(annual_path, index_col=0)
    return df


@pytest.fixture
def annual_stockrow_bs_stmt_cat() -> FinStatementsBase:
    stmt = FinStatementsBase.from_df(annual_stockrow_bs_df_cat(), BALANCE_SHEET_INPUT_CONFIG.display_name, BALANCE_SHEET_INPUT_CONFIG.items_config_list)
    return stmt


@pytest.fixture
def annual_stockrow_stmts_cat(
    annual_stockrow_income_stmt_cat, annual_stockrow_bs_stmt_cat
) -> FinancialStatements:
    stmts = FinancialStatements(
        annual_stockrow_income_stmt_cat, annual_stockrow_bs_stmt_cat
    )
    return stmts


def quarterly_stockrow_income_df_cat() -> pd.DataFrame:
    quarterly_path = os.path.join(CAT_PATH, "quarterly_income.csv")
    df = pd.read_csv(quarterly_path, index_col=0)
    return df


@pytest.fixture
def quarterly_stockrow_income_stmt_cat() -> FinStatementsBase:
    stmt = FinStatementsBase.from_df(quarterly_stockrow_income_df_cat(), INCOME_STATEMENT_CONFIG.display_name, INCOME_STATEMENT_CONFIG.items_config_list)
    return stmt


def quarterly_stockrow_bs_df_cat() -> pd.DataFrame:
    quarterly_path = os.path.join(CAT_PATH, "quarterly_bs.csv")
    df = pd.read_csv(quarterly_path, index_col=0)
    return df


@pytest.fixture
def quarterly_stockrow_bs_stmt_cat() -> FinStatementsBase:
    stmt = FinStatementsBase.from_df(quarterly_stockrow_bs_df_cat(), BALANCE_SHEET_INPUT_CONFIG.display_name, BALANCE_SHEET_INPUT_CONFIG.items_config_list)
    return stmt


@pytest.fixture
def quarterly_stockrow_stmts_cat(
    quarterly_stockrow_income_stmt_cat, quarterly_stockrow_bs_stmt_cat
) -> FinancialStatements:
    stmts = FinancialStatements(
        quarterly_stockrow_income_stmt_cat, quarterly_stockrow_bs_stmt_cat
    )
    return stmts
