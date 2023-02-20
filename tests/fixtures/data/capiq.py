import os

import pandas as pd
import pytest

from finstmt import BalanceSheets, FinancialStatements, IncomeStatements
from finstmt.exc import MismatchingDatesException
from finstmt.loaders.capiq import load_capiq_df
from tests.fixtures.data.common import DATA_PATH

CAPIQ_PATH = os.path.join(DATA_PATH, "capiq")


def annual_capiq_income_df() -> pd.DataFrame:
    path = os.path.join(CAPIQ_PATH, "annual_cat.xls")
    sheet_name = "Income Statement"
    df = load_capiq_df(path, sheet_name)
    return df


@pytest.fixture(scope="session")
def annual_capiq_income_stmt() -> IncomeStatements:
    stmt = IncomeStatements.from_df(annual_capiq_income_df())
    return stmt


def annual_capiq_bs_df() -> pd.DataFrame:
    path = os.path.join(CAPIQ_PATH, "annual_cat.xls")
    sheet_name = "Balance Sheet"
    df = load_capiq_df(path, sheet_name)
    return df


@pytest.fixture(scope="session")
def annual_capiq_bs_stmt() -> BalanceSheets:
    stmt = BalanceSheets.from_df(annual_capiq_bs_df())
    return stmt


def _annual_capiq_stmts(
    annual_capiq_income_stmt, annual_capiq_bs_stmt
) -> FinancialStatements:
    try:
        stmts = FinancialStatements(annual_capiq_income_stmt, annual_capiq_bs_stmt)
    except MismatchingDatesException:
        pass
    else:
        assert False
    dates = annual_capiq_income_stmt.dates
    stmts = FinancialStatements(annual_capiq_income_stmt, annual_capiq_bs_stmt[dates])
    return stmts


@pytest.fixture
def annual_capiq_stmts(
    annual_capiq_income_stmt, annual_capiq_bs_stmt
) -> FinancialStatements:
    return _annual_capiq_stmts(annual_capiq_income_stmt, annual_capiq_bs_stmt)


@pytest.fixture(scope="session")
def ro_annual_capiq_stmts(
    annual_capiq_income_stmt, annual_capiq_bs_stmt
) -> FinancialStatements:
    return _annual_capiq_stmts(annual_capiq_income_stmt, annual_capiq_bs_stmt)


def quarterly_capiq_income_df() -> pd.DataFrame:
    path = os.path.join(CAPIQ_PATH, "quarterly_cat.xls")
    sheet_name = "Income Statement"
    df = load_capiq_df(path, sheet_name)
    return df


@pytest.fixture
def quarterly_capiq_income_stmt() -> IncomeStatements:
    stmt = IncomeStatements.from_df(quarterly_capiq_income_df())
    return stmt


def quarterly_capiq_bs_df() -> pd.DataFrame:
    path = os.path.join(CAPIQ_PATH, "quarterly_cat.xls")
    sheet_name = "Balance Sheet"
    df = load_capiq_df(path, sheet_name)
    return df


@pytest.fixture
def quarterly_capiq_bs_stmt() -> BalanceSheets:
    stmt = BalanceSheets.from_df(quarterly_capiq_bs_df())
    return stmt


@pytest.fixture
def quarterly_capiq_stmts(
    quarterly_capiq_income_stmt, quarterly_capiq_bs_stmt
) -> FinancialStatements:
    stmts = FinancialStatements(quarterly_capiq_income_stmt, quarterly_capiq_bs_stmt)
    return stmts
