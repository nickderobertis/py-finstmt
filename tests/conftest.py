import pytest
import os
import pandas as pd

DATA_PATH = os.path.sep.join(['tests', 'sources'])
STOCKROW_PATH = os.path.join(DATA_PATH, 'stockrow')


@pytest.fixture
def annual_stockrow_income_df() -> pd.DataFrame:
    annual_path = os.path.join(STOCKROW_PATH, 'annual_income.csv')
    df = pd.read_csv(annual_path, index_col=0)
    return df


@pytest.fixture
def annual_stockrow_bs_df() -> pd.DataFrame:
    annual_path = os.path.join(STOCKROW_PATH, 'annual_bs.csv')
    df = pd.read_csv(annual_path, index_col=0)
    return df


@pytest.fixture
def quarterly_stockrow_income_df() -> pd.DataFrame:
    quarterly_path = os.path.join(STOCKROW_PATH, 'quarterly_income.csv')
    df = pd.read_csv(quarterly_path, index_col=0)
    return df


@pytest.fixture
def quarterly_stockrow_bs_df() -> pd.DataFrame:
    quarterly_path = os.path.join(STOCKROW_PATH, 'quarterly_bs.csv')
    df = pd.read_csv(quarterly_path, index_col=0)
    return df