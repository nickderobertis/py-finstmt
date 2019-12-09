import pytest
import os
import pandas as pd

from finstmt import IncomeStatements, BalanceSheets, FinancialStatements
from tests.fixtures.data.common import DATA_PATH
from finstmt.loaders.capiq import load_capiq_df

CAPIQ_PATH = os.path.join(DATA_PATH, 'capiq')

@pytest.fixture
def annual_capiq_income_df() -> pd.DataFrame:
    path = os.path.join(CAPIQ_PATH, 'annual_cat.xls')
    sheet_name = 'Income Statement'
    df = load_capiq_df(path, sheet_name)
    return df


@pytest.fixture
def annual_capiq_bs_df() -> pd.DataFrame:
    path = os.path.join(CAPIQ_PATH, 'annual_cat.xls')
    sheet_name = 'Balance Sheet'
    df = load_capiq_df(path, sheet_name)
    return df


@pytest.fixture
def quarterly_capiq_income_df() -> pd.DataFrame:
    path = os.path.join(CAPIQ_PATH, 'quarterly_cat.xls')
    sheet_name = 'Income Statement'
    df = load_capiq_df(path, sheet_name)
    return df


@pytest.fixture
def quarterly_capiq_bs_df() -> pd.DataFrame:
    path = os.path.join(CAPIQ_PATH, 'quarterly_cat.xls')
    sheet_name = 'Balance Sheet'
    df = load_capiq_df(path, sheet_name)
    return df
