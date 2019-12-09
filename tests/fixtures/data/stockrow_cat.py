import pytest
import os
import pandas as pd

from finstmt import IncomeStatements, BalanceSheets, FinancialStatements
from tests.fixtures.data.common import DATA_PATH

STOCKROW_PATH = os.path.join(DATA_PATH, 'stockrow')
CAT_PATH = os.path.join(STOCKROW_PATH, 'CAT')


@pytest.fixture
def annual_stockrow_income_df_cat() -> pd.DataFrame:
    annual_path = os.path.join(CAT_PATH, 'annual_income.csv')
    df = pd.read_csv(annual_path, index_col=0)
    return df


@pytest.fixture
def annual_stockrow_income_stmt_cat(annual_stockrow_income_df_cat) -> IncomeStatements:
    stmt = IncomeStatements.from_df(annual_stockrow_income_df_cat)
    return stmt


@pytest.fixture
def annual_stockrow_bs_df_cat() -> pd.DataFrame:
    annual_path = os.path.join(CAT_PATH, 'annual_bs.csv')
    df = pd.read_csv(annual_path, index_col=0)
    return df


@pytest.fixture
def annual_stockrow_bs_stmt_cat(annual_stockrow_bs_df_cat) -> BalanceSheets:
    stmt = BalanceSheets.from_df(annual_stockrow_bs_df_cat)
    return stmt


@pytest.fixture
def annual_stockrow_stmts_cat(annual_stockrow_income_stmt_cat, annual_stockrow_bs_stmt_cat) -> FinancialStatements:
    stmts = FinancialStatements(annual_stockrow_income_stmt_cat, annual_stockrow_bs_stmt_cat)
    return stmts


@pytest.fixture
def quarterly_stockrow_income_df_cat() -> pd.DataFrame:
    quarterly_path = os.path.join(CAT_PATH, 'quarterly_income.csv')
    df = pd.read_csv(quarterly_path, index_col=0)
    return df


@pytest.fixture
def quarterly_stockrow_income_stmt_cat(quarterly_stockrow_income_df_cat) -> IncomeStatements:
    stmt = IncomeStatements.from_df(quarterly_stockrow_income_df_cat)
    return stmt


@pytest.fixture
def quarterly_stockrow_bs_df_cat() -> pd.DataFrame:
    quarterly_path = os.path.join(CAT_PATH, 'quarterly_bs.csv')
    df = pd.read_csv(quarterly_path, index_col=0)
    return df


@pytest.fixture
def quarterly_stockrow_bs_stmt_cat(quarterly_stockrow_bs_df_cat) -> BalanceSheets:
    stmt = BalanceSheets.from_df(quarterly_stockrow_bs_df_cat)
    return stmt


@pytest.fixture
def quarterly_stockrow_stmts_cat(quarterly_stockrow_income_stmt_cat, quarterly_stockrow_bs_stmt_cat) -> FinancialStatements:
    stmts = FinancialStatements(quarterly_stockrow_income_stmt_cat, quarterly_stockrow_bs_stmt_cat)
    return stmts