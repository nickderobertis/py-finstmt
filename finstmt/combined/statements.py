import operator
from copy import deepcopy
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Callable

import pandas as pd
from sympy import Indexed

from finstmt import BalanceSheets, IncomeStatements
from finstmt.config_manage.statements import StatementsConfigManager
from finstmt.exc import MismatchingDatesException
from finstmt.findata.statementsbase import FinStatementsBase
from finstmt.forecast.config import ForecastConfig
from finstmt.forecast.main import Forecast
from finstmt.items.config import ItemConfig


@dataclass
class FinancialStatements:
    """
    Main class that holds all the financial statements.

    Examples:
        >>> bs_path = r'WMT Balance Sheet.xlsx'
        >>> inc_path = r'WMT Income Statement.xlsx'
        >>> bs_df = pd.read_excel(bs_path)
        >>> inc_df = pd.read_excel(inc_path)
        >>> bs_data = BalanceSheets.from_df(bs_df)
        >>> inc_data = IncomeStatements.from_df(inc_df)
        >>> stmts = FinancialStatements(inc_data, bs_data)
    """
    income_statements: IncomeStatements
    balance_sheets: BalanceSheets
    calculate: bool = True


    def __post_init__(self):
        from finstmt.resolver.history import StatementsResolver

        self._create_config_from_statements()

        if self.calculate:
            resolver = StatementsResolver(self)
            new_stmts = resolver.to_statements()
            self.income_statements = new_stmts.income_statements
            self.balance_sheets = new_stmts.balance_sheets
            self._create_config_from_statements()

    def _create_config_from_statements(self):
        config_dict = {}
        config_dict['income_statements'] = self.income_statements.config
        config_dict['balance_sheets'] = self.balance_sheets.config
        self.config = StatementsConfigManager(config_dict)

    def change(self, data_key: str) -> pd.Series:
        """
        Get the change between this period and last for a data series

        :param data_key: key of variable, how it would be accessed with FinancialStatements.data_key
        """
        series = getattr(self, data_key)
        return series - self.lag(data_key, 1)

    def lag(self, data_key: str, num_lags: int) -> pd.Series:
        """
        Get a data series lagged for a number of periods

        :param data_key: key of variable, how it would be accessed with FinancialStatements.data_key
        :param num_lags: Number of lags
        """
        series = getattr(self, data_key)
        return series.shift(num_lags)

    def _repr_html_(self):
        return f"""
        <h2>Income Statement</h2>
        {self.income_statements._repr_html_()}
        <h2>Balance Sheet</h2>
        {self.balance_sheets._repr_html_()}
        """

    def __getattr__(self, item):
        inc_items = dir(super().__getattribute__('income_statements'))
        bs_items = dir(super().__getattribute__('balance_sheets'))
        if item not in inc_items + bs_items:
            raise AttributeError(item)

        if item in inc_items:
            return getattr(self.income_statements, item)

        # in balance sheet items
        return getattr(self.balance_sheets, item)

    def __getitem__(self, item):
        if not isinstance(item, (list, tuple)):
            inc_statement = self.income_statements[item]
            bs = self.balance_sheets[item]
            date_item = pd.to_datetime(item)
            inc_statements = IncomeStatements({date_item: inc_statement})
            b_sheets = BalanceSheets({date_item: bs})
        else:
            inc_statements = self.income_statements[item]
            b_sheets = self.balance_sheets[item]

        return FinancialStatements(inc_statements, b_sheets)

    def __dir__(self):
        normal_attrs = [
            'income_statements',
            'balance_sheets',
            'capex',
            'non_cash_expenses',
            'fcf',
            'forecast',
            'forecasts',
            'forecast_assumptions',
            'dates',
            'copy',
        ]
        all_config = self.income_statements.config.items + self.balance_sheets.config.items
        item_attrs = [config.key for config in all_config]
        return normal_attrs + item_attrs

    @property
    def capex(self) -> pd.Series:
        return self.change('net_ppe') + self.dep

    @property
    def non_cash_expenses(self) -> pd.Series:
        # TODO [#5]: add stock-based compensation and use in non-cash expenses calculation
        return self.dep + self.gain_on_sale_invest + self.gain_on_sale_asset + self.impairment

    @property
    def fcf(self) -> pd.Series:
        return self.net_income + self.non_cash_expenses - self.change('nwc') - self.capex

    def forecast(self, **kwargs) -> 'FinancialStatements':
        from finstmt.resolver.forecast import ForecastResolver

        if 'bs_diff_max' in kwargs:
            bs_diff_max = kwargs['bs_diff_max']
        else:
            bs_diff_max = ForecastConfig.bs_diff_max

        if 'balance' in kwargs:
            balance = kwargs['balance']
        else:
            balance = ForecastConfig.balance

        self._validate_dates()

        all_forecast_dict = {}
        all_results = {}
        for stmt in [self.income_statements, self.balance_sheets]:
            forecast_dict, results = stmt._forecast(self, **kwargs)
            all_forecast_dict.update(forecast_dict)
            all_results.update(results)

        resolver = ForecastResolver(self, all_forecast_dict, all_results, bs_diff_max, balance=balance)
        obj = resolver.to_statements()

        return obj

    @property
    def forecast_assumptions(self) -> pd.DataFrame:
        all_series = []
        for config in self.all_config_items:
            if not config.forecast_config.make_forecast:
                continue
            config_series = config.forecast_config.to_series()
            config_series.name = config.display_name
            all_series.append(config_series)
        return pd.concat(all_series, axis=1).T

    @property
    def all_config_items(self) -> List[ItemConfig]:
        return self.income_statements.config.items + self.balance_sheets.config.items  # type: ignore

    @property
    def dates(self) -> List[pd.Timestamp]:
        self._validate_dates()
        return list(self.balance_sheets.statements.keys())

    def _validate_dates(self):
        bs_dates = set(self.balance_sheets.statements.keys())
        is_dates = set(self.income_statements.statements.keys())
        if bs_dates != is_dates:
            bs_unique = bs_dates.difference(is_dates)
            is_unique = is_dates.difference(bs_dates)
            message = 'Got mismatching dates between historical statements. '
            if bs_unique:
                message += f'Balance sheet has {bs_unique} dates not in Income Statement. '
            if is_unique:
                message += f'Income Statement has {is_unique} dates not in Balance Sheet. '
            raise MismatchingDatesException(message)

    def copy(self) -> 'FinancialStatements':
        return deepcopy(self)

    def __add__(self, other):
        statements = _combine_statements(self, other, operator.add)
        return _new_statements(self, other, *statements)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        statements = _combine_statements(self, other, operator.sub)
        return _new_statements(self, other, *statements)

    def __rsub__(self, other):
        return (-1 * self) + other

    def __mul__(self, other):
        statements = _combine_statements(self, other, operator.mul)
        return _new_statements(self, other, *statements)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        statements = _combine_statements(self, other, operator.truediv)
        return _new_statements(self, other, *statements)

    def __rtruediv__(self, other):
        # TODO [#41]: implement right division for statements
        raise NotImplementedError(f'cannot divide type {type(other)} by type {type(self)}')


def _combine_statements(statements: FinancialStatements,
                        other_statements: FinancialStatements,
                        func: Callable) -> Tuple[IncomeStatements, BalanceSheets]:
    if isinstance(other_statements, (float, int)):
        new_inc_df = func(statements.income_statements.df, other_statements)
        new_inc = IncomeStatements.from_df(
            new_inc_df, statements.income_statements.config.items, disp_unextracted=False
        )
        new_bs_df = func(statements.balance_sheets.df, other_statements)
        new_bs = BalanceSheets.from_df(
            new_bs_df, statements.balance_sheets.config.items, disp_unextracted=False
        )
    elif isinstance(other_statements, FinancialStatements):
        new_inc = func(statements.income_statements, other_statements.income_statements)
        new_bs = func(statements.balance_sheets, other_statements.balance_sheets)
    else:
        raise NotImplementedError(f'cannot {func.__name__} type {type(statements)} to type {type(other_statements)}')

    return new_inc, new_bs

def _new_statements(statements: FinancialStatements, other_statements: FinancialStatements,
                    new_inc: IncomeStatements, new_bs: BalanceSheets) -> FinancialStatements:
    from finstmt.forecast.statements import ForecastedFinancialStatements
    if isinstance(statements, ForecastedFinancialStatements) and isinstance(other_statements, ForecastedFinancialStatements):
        raise NotImplementedError('not yet implemented to combine two forecasted statements')
    if isinstance(statements, ForecastedFinancialStatements):
        return ForecastedFinancialStatements(new_inc, new_bs, statements.forecasts)  # type: ignore
    if isinstance(other_statements, ForecastedFinancialStatements):
        return ForecastedFinancialStatements(new_inc, new_bs, other_statements.forecasts)  # type: ignore

    return FinancialStatements(new_inc, new_bs)
