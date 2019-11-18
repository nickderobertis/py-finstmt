from dataclasses import dataclass, field
from typing import Dict

import pandas as pd

from finstmt import BalanceSheets, IncomeStatements
from finstmt.forecast.config import ForecastConfig
from finstmt.forecast.main import Forecast


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

    forecasts: Dict[str, Forecast] = field(default_factory=lambda: {})


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
        inc_items = dir(self.income_statements)
        bs_items = dir(self.balance_sheets)
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
            'fcf'
        ]
        all_config = self.income_statements.statement_cls.items_config + self.balance_sheets.statement_cls.items_config
        item_attrs = [config.key for config in all_config]
        return normal_attrs + item_attrs

    @property
    def capex(self) -> pd.Series:
        return self.change('net_ppe') + self.dep

    @property
    def non_cash_expenses(self) -> pd.Series:
        # TODO: add stock-based compensation once it is in the data
        return self.dep + self.gain_on_sale_invest + self.gain_on_sale_asset + self.impairment

    @property
    def fcf(self) -> pd.Series:
        return self.net_income + self.non_cash_expenses - self.change('nwc') - self.capex

    def forecast(self, **kwargs) -> 'FinancialStatements':
        all_forecast_dict = {}
        all_results = {}
        all_pct_results = {}
        for stmt in [self.income_statements, self.balance_sheets]:
            forecast_dict, results, pct_results = stmt._forecast(self, **kwargs)
            all_forecast_dict.update(forecast_dict)
            all_results.update(results)
            all_pct_results.update(pct_results)

        # Resolve pct of items
        for pct_item_key, pct_result in all_pct_results.items():
            # TODO: replace with config manager get
            all_configs = self.income_statements.statement_cls.items_config + self.balance_sheets.statement_cls.items_config
            item_config = [conf for conf in all_configs if conf.key == pct_item_key][0]
            # TODO: may need retry behavior here and multiple loops through items to resolve everything
            # TODO: also taking a percentage of a calculated item won't work as they are calculated in the class
            pct_of_series = all_results[item_config.forecast_config.pct_of]
            calc_series = pct_result * pct_of_series
            calc_series.name = pct_result.name
            all_results[pct_item_key] = calc_series

        all_results = pd.concat(list(all_results.values()), axis=1).T
        inc_df = self.income_statements.__class__.from_df(all_results)
        bs_df = self.balance_sheets.__class__.from_df(all_results)
        obj = self.__class__(inc_df, bs_df)
        obj.forecasts = all_forecast_dict
        return obj

    @property
    def forecast_assumptions(self) -> pd.DataFrame:
        # TODO: replace with config manager get
        all_configs = self.income_statements.statement_cls.items_config + self.balance_sheets.statement_cls.items_config
        all_series = []
        for config in all_configs:
            if config.extract_names is None or not config.forecast_config.make_forecast:
                continue
            config_series = config.forecast_config.to_series()
            config_series.name = config.display_name
            all_series.append(config_series)
        return pd.concat(all_series, axis=1).T


