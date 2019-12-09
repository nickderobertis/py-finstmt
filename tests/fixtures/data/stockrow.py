import pytest
import os
import pandas as pd

from finstmt import IncomeStatements, BalanceSheets, FinancialStatements
from tests.fixtures.data.common import DATA_PATH

STOCKROW_PATH = os.path.join(DATA_PATH, 'stockrow')


@pytest.fixture
def annual_stockrow_income_df() -> pd.DataFrame:
    annual_path = os.path.join(STOCKROW_PATH, 'annual_income.csv')
    df = pd.read_csv(annual_path, index_col=0)
    return df


@pytest.fixture
def annual_stockrow_income_stmt(annual_stockrow_income_df) -> IncomeStatements:
    stmt = IncomeStatements.from_df(annual_stockrow_income_df)
    return stmt


@pytest.fixture
def annual_stockrow_bs_df() -> pd.DataFrame:
    annual_path = os.path.join(STOCKROW_PATH, 'annual_bs.csv')
    df = pd.read_csv(annual_path, index_col=0)
    return df


@pytest.fixture
def annual_stockrow_bs_stmt(annual_stockrow_bs_df) -> BalanceSheets:
    stmt = BalanceSheets.from_df(annual_stockrow_bs_df)
    return stmt


@pytest.fixture
def annual_stockrow_stmts(annual_stockrow_income_stmt, annual_stockrow_bs_stmt) -> FinancialStatements:
    stmts = FinancialStatements(annual_stockrow_income_stmt, annual_stockrow_bs_stmt)
    return stmts


@pytest.fixture
def quarterly_stockrow_income_df() -> pd.DataFrame:
    quarterly_path = os.path.join(STOCKROW_PATH, 'quarterly_income.csv')
    df = pd.read_csv(quarterly_path, index_col=0)
    return df


@pytest.fixture
def quarterly_stockrow_income_stmt(quarterly_stockrow_income_df) -> IncomeStatements:
    stmt = IncomeStatements.from_df(quarterly_stockrow_income_df)
    return stmt


@pytest.fixture
def quarterly_stockrow_bs_df() -> pd.DataFrame:
    quarterly_path = os.path.join(STOCKROW_PATH, 'quarterly_bs.csv')
    df = pd.read_csv(quarterly_path, index_col=0)
    return df


@pytest.fixture
def quarterly_stockrow_bs_stmt(quarterly_stockrow_bs_df) -> BalanceSheets:
    stmt = BalanceSheets.from_df(quarterly_stockrow_bs_df)
    return stmt


@pytest.fixture
def quarterly_stockrow_stmts(quarterly_stockrow_income_stmt, quarterly_stockrow_bs_stmt) -> FinancialStatements:
    stmts = FinancialStatements(quarterly_stockrow_income_stmt, quarterly_stockrow_bs_stmt)
    return stmts