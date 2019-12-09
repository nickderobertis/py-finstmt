"""
Use these functions to help generate data for loading tests

Examples:
    >>> from finstmt import FinancialStatements, IncomeStatements, BalanceSheets
    >>> import pandas as pd
    >>> import os
    >>> from tests.utils.gen.data_load import print_test_data_def, get_keys_for_inc_data_items, get_keys_for_bs_data_items
    >>>
    >>> DATA_PATH = os.path.sep.join(['tests', 'sources'])
    >>> STOCKROW_PATH = os.path.join(DATA_PATH, 'stockrow')
    >>>
    >>> inc_path = os.path.join(STOCKROW_PATH, 'annual_income.csv')
    >>> inc_df = pd.read_csv(inc_path, index_col=0)
    >>>
    >>> bs_path = os.path.join(STOCKROW_PATH, 'annual_bs.csv')
    >>> bs_df = pd.read_csv(bs_path, index_col=0)
    >>>
    >>> bs = BalanceSheets.from_df(bs_df)
    >>> inc = IncomeStatements.from_df(inc_df)
    >>> stmts = FinancialStatements(inc, bs)
    >>>
    >>> inc_keys = get_keys_for_inc_data_items()
    >>> bs_keys = get_keys_for_bs_data_items()
    >>>
    >>> print_test_data_def(stmts, inc_keys + bs_keys, 'a_index', 'a_test_data_dict')
"""

from typing import List

from finstmt import IncomeStatements, BalanceSheets, FinancialStatements


def get_keys_for_inc_data_items() -> List[str]:
    return [item.key for item in IncomeStatements.statement_cls.items_config]


def get_keys_for_bs_data_items() -> List[str]:
    return [item.key for item in BalanceSheets.statement_cls.items_config]


def print_test_data_def(stmts: FinancialStatements, data_keys: List[str], index_name: str = 'a_index',
                         data_dict_name: str = 'a_test_data_dict') -> None:
    _print_index_def(stmts, data_keys, index_name)
    _print_data_dict_def(stmts, data_keys, index_name, data_dict_name)


def _print_data_dict_def(stmts: FinancialStatements, data_keys: List[str], index_name: str = 'a_index',
                         data_dict_name: str = 'a_test_data_dict') -> None:
    print(f'{data_dict_name} = dict(')
    for key in data_keys:
        value = getattr(stmts, key).values
        str_value = '[' + ', '.join([str(val) for val in value]) + ']'
        print(f'\t{key}=pd.Series(\n\t\t{str_value},\n\t\tindex={index_name}\n\t),')
    print(')')


def _print_index_def(stmts: FinancialStatements, data_keys: List[str], index_name: str = 'a_index') -> None:
    index_values_str = '[' + ', '.join([f'"{val}"' for val in getattr(stmts, data_keys[0]).index]) + ']'
    print(f'{index_name}_str = {index_values_str}')
    print(f'{index_name} = [pd.to_datetime(val) for val in {index_name}_str]')
