from dataclasses import dataclass, field
from typing import Dict

import pandas as pd
from sympy import Indexed

from finstmt import BalanceSheets, IncomeStatements
from finstmt.config_manage.statements import StatementsConfigManager
from finstmt.findata.statementsbase import FinStatementsBase
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


    def __post_init__(self):
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
            'fcf',
            'forecast',
            'forecast_assumptions',
        ]
        all_config = self.income_statements.statement_cls.items_config + self.balance_sheets.statement_cls.items_config
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
        from finstmt.forecast.statements import ForecastedFinancialStatements

        # TODO [#6]: clean up forecast logic
        #
        # Seems like this whole thing is repeating a lot of logic that could maybe be removed if
        # I could construct partial financial statements.
        #
        # Restructuring the sympy variables integration into its own library could help.
        #
        # This code also feels very messy in general.
        all_forecast_dict = {}
        all_results = {}
        all_pct_results = {}
        for stmt in [self.income_statements, self.balance_sheets]:
            forecast_dict, results, pct_results = stmt._forecast(self, **kwargs)
            all_forecast_dict.update(forecast_dict)
            all_results.update(results)
            all_pct_results.update(pct_results)

        # Set up for creating dictionary for sympy substitutions. First extract all the results into a dict of dicts
        # nested dict where keys are date indices, values are dicts where keys are item keys, values are item values
        by_date_item_dict: Dict[pd.Timestamp, Dict[str, float]] = {}
        all_dates = list(all_results.values())[0].index.tolist()

        def add_series_to_by_date_item_dict(series: pd.Series, item_key: str):
            for date, value in series.iteritems():
                date_idx = all_dates.index(date)
                if date_idx not in by_date_item_dict:
                    by_date_item_dict[date_idx] = {}
                by_date_item_dict[date_idx][item_key] = value

        [add_series_to_by_date_item_dict(result_series, item_key) for item_key, result_series in all_results.items()]
        t = self.config.sympy_namespace['t']

        def get_subs_dict(t_offset: int):
            subs_dict = {}
            # TODO [#7]: in forecast calculation process, need to grab previous values
            #
            # Currently only getting current period values.
            values_dict = by_date_item_dict[t_offset]
            for item_key, item_symbol in self.config.sympy_namespace.items():
                if item_key in values_dict:
                    indexed_symbol = item_symbol.__getitem__(t)  # eg cash[t] or cash[t-1]
                    subs_dict[indexed_symbol] = values_dict[item_key]
            return subs_dict

        def get_expr_eval_create_series_and_add_to_by_date_item_dict_and_results(overall_item_key: str) -> pd.Series:
            result_dict = {}
            expr = self.config.expr_for(overall_item_key)
            for i, date in enumerate(all_dates):
                # Now create the subs dict from the dict of dicts
                subs_dict = get_subs_dict(i)
                substituted = expr.subs(subs_dict)
                try:
                    eval_expr = float(substituted)
                except TypeError:
                    # This means wasn't completely substituted. Must be a calculated item which has not yet
                    # been calculated. Calculate it now.
                    reverse_sympy_ns = {value: key for key, value in self.config.sympy_namespace.items()}
                    for sym in substituted.free_symbols:
                        if isinstance(sym, Indexed):
                            # Got an uncalculated symbol
                            uncalc_key = reverse_sympy_ns[sym.base]
                            get_expr_eval_create_series_and_add_to_by_date_item_dict_and_results(uncalc_key)
                    # Now try the original calculation again, now that missing items have been calculated
                    subs_dict = get_subs_dict(i)
                    substituted = expr.subs(subs_dict)
                    eval_expr = float(substituted)
                result_dict[date] = eval_expr
            result_series = pd.Series(result_dict)
            result_series.name = self.config.get_value(overall_item_key, 'primary_name')
            # Add this newly calculated series to overall substitution values
            add_series_to_by_date_item_dict(result_series, overall_item_key)
            all_results[overall_item_key] = result_series
            return result_series

        # Resolve pct of items
        for pct_item_key, pct_result in all_pct_results.items():
            item_config = self.config.get(pct_item_key)
            pct_of_key = item_config.forecast_config.pct_of
            pct_of_config, pct_of_source_key = self.config._get(pct_of_key)
            if pct_of_key in all_results:
                # Already have result, just get it from results
                pct_of_series = all_results[item_config.forecast_config.pct_of]
            elif pct_of_config.expr_str is not None:
                # This is a calculated item, need to calculate it, add it to results, and use that series
                pct_of_series = get_expr_eval_create_series_and_add_to_by_date_item_dict_and_results(pct_of_key)
            else:
                raise ValueError(f'could not get series for {pct_of_key}')
            calc_series = pct_result * pct_of_series
            calc_series.name = pct_result.name
            all_results[pct_item_key] = calc_series
            # Add this newly calculated series to overall substitution values
            add_series_to_by_date_item_dict(calc_series, pct_item_key)

        all_results = pd.concat(list(all_results.values()), axis=1).T
        inc_df = self.income_statements.__class__.from_df(all_results)
        bs_df = self.balance_sheets.__class__.from_df(all_results)

        # type ignore added because for some reason mypy is not picking up structure
        # correctly since it is a dataclass
        obj = ForecastedFinancialStatements(inc_df, bs_df, all_forecast_dict)  # type: ignore
        return obj

    @property
    def forecast_assumptions(self) -> pd.DataFrame:
        all_configs = self.income_statements.statement_cls.items_config + self.balance_sheets.statement_cls.items_config  # type: ignore
        all_series = []
        for config in all_configs:
            if config.extract_names is None or not config.forecast_config.make_forecast:
                continue
            config_series = config.forecast_config.to_series()
            config_series.name = config.display_name
            all_series.append(config_series)
        return pd.concat(all_series, axis=1).T


