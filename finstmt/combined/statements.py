import dataclasses
from dataclasses import dataclass
from typing import TYPE_CHECKING, List, Optional, Set

import pandas as pd
from typing_extensions import Self

from finstmt.bs.main import BalanceSheets
from finstmt.check import item_series_is_empty
from finstmt.combined.combinator import (
    FinancialStatementsCombinator,
    StatementsCombinator,
)
from finstmt.config.statement_config import StatementConfig
from finstmt.config_manage.data import DataConfigManager
from finstmt.config_manage.statements import StatementsConfigManager
from finstmt.exc import MismatchingDatesException
from finstmt.findata.statementsbase import FinStatementsBase
from finstmt.forecast.config import ForecastConfig
from finstmt.inc.main import IncomeStatements
from finstmt.items.config import ItemConfig
from finstmt.logger import logger

if TYPE_CHECKING:
    from finstmt.forecast.statements import ForecastedFinancialStatements


@dataclass
class FinancialStatements:
    """
    Main class that holds all the financial statements.

    :param auto_adjust_config: Whether to automatically adjust the configuration based
        on the loaded data. Currently will turn forecasting off for items not in the data,
        and turn forecasting on for items normally calculated off those which are
        not in the data. For example, if gross_ppe is missing then will start forecasting
        net_ppe instead

    Examples:
        >>> bs_path = r'WMT Balance Sheet.xlsx'
        >>> inc_path = r'WMT Income Statement.xlsx'
        >>> bs_df = pd.read_excel(bs_path)
        >>> inc_df = pd.read_excel(inc_path)
        >>> bs_data = BalanceSheets.from_df(bs_df)
        >>> inc_data = IncomeStatements.from_df(inc_df)
        >>> stmts = FinancialStatements(inc_data, bs_data)
    """

    # income_statements: IncomeStatements
    # balance_sheets: BalanceSheets
    statements: List[FinStatementsBase]
    calculate: bool = True
    auto_adjust_config: bool = True
    _combinator: StatementsCombinator[Self] = FinancialStatementsCombinator()  # type: ignore[assignment]

    def __post_init__(self):
        from finstmt.resolver.history import StatementsResolver

        self._create_config_from_statements()

        if self.calculate:
            resolver = StatementsResolver(self)
            new_stmts = resolver.to_statements(
                auto_adjust_config=self.auto_adjust_config
            )
            self.statements = new_stmts.statements
            # self.income_statements = new_stmts.income_statements
            # self.balance_sheets = new_stmts.balance_sheets
            self._create_config_from_statements()

    def _create_config_from_statements(self):
        config_dict = {}
        for stmt_timeseries in self.statements:
            config_dict[stmt_timeseries.statement_name] = stmt_timeseries.config
        # config_dict["income_statements"] = self.income_statements.config
        # config_dict["balance_sheets"] = self.balance_sheets.config
        self.config = StatementsConfigManager(config_managers=config_dict)
        if self.auto_adjust_config:
            self._adjust_config_based_on_data()

    def _adjust_config_based_on_data(self):
        for item in self.config.items:
            if self.item_is_empty(item.key):
                if self.config.get(item.key).forecast_config.plug:
                    # It is OK for plug items to be empty, won't affect the forecast
                    continue

                # Useless to make forecasts on empty items
                logger.debug(f"Setting {item.key} to not forecast as it is empty")
                item.forecast_config.make_forecast = False
                # But this may mean another item should be forecasted instead.
                # E.g. normally net_ppe is calculated from gross_ppe and dep,
                # so it is not forecasted. But if gross_ppe is missing from
                # the data, then net_ppe should be forecasted directly.

                # So first, get the equations involving this item to determine
                # what other items are related to this one
                relevant_eqs = self.config.eqs_involving(item.key)
                relevant_keys: Set[str] = {item.key}
                for eq in relevant_eqs:
                    relevant_keys.add(self.config._expr_to_keys(eq.lhs)[0])
                    relevant_keys.update(set(self.config._expr_to_keys(eq.rhs)))
                relevant_keys.remove(item.key)
                for key in relevant_keys:
                    if self.item_is_empty(key):
                        continue
                    conf = self.config.get(key)
                    if conf.expr_str is None:
                        # Not a calculated item, so it doesn't make sense to turn forecasting on
                        continue

                    # Check to make sure that all components of the calculated item are also empty
                    expr = self.config.expr_for(key)
                    component_keys = self.config._expr_to_keys(expr)
                    all_component_items_are_empty = True
                    for c_key in component_keys:
                        if not self.item_is_empty(c_key):
                            all_component_items_are_empty = False
                    if not all_component_items_are_empty:
                        continue
                    # Now this is a calculated item which is non-empty, and all the components of the
                    # calculated are empty, so we need to forecast this item instead
                    logger.debug(
                        f"Setting {conf.key} to forecast as it is a calculated item which is not empty "
                        f"and yet none of the components have data"
                    )
                    conf.forecast_config.make_forecast = True

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

    def item_is_empty(self, data_key: str) -> bool:
        """
        Whether the passed item has no data

        :param data_key: key of variable, how it would be accessed with FinancialStatements.data_key
        :return:
        """
        series = getattr(self, data_key)
        return item_series_is_empty(series)

    def _repr_html_(self):
        result = ""
        for stmt_timeseries in self.statements:
            result += f"""
            <h2>{stmt_timeseries.statement_name}</h2>
            {stmt_timeseries._repr_html_()}
            """
        return result
        # return f"""
        # <h2>Income Statement</h2>
        # {self.income_statements._repr_html_()}
        # <h2>Balance Sheet</h2>
        # {self.balance_sheets._repr_html_()}
        # """

    def __getattr__(self, item):
        for stmt in self.statements:
            if item in dir(stmt):
                return getattr(stmt, item)

        raise AttributeError(item)

        # inc_items = dir(super().__getattribute__("income_statements"))
        # bs_items = dir(super().__getattribute__("balance_sheets"))
        # if item not in inc_items + bs_items:
        #     raise AttributeError(item)

        # if item in inc_items:
        #     return getattr(self.income_statements, item)

        # # in balance sheet items
        # return getattr(self.balance_sheets, item)

    def __getitem__(self, item):
        print(item)
        stmts_hetrogeneous = []
        if not isinstance(item, (list, tuple)):
            date_item = pd.to_datetime(item)
            for stmt_timeseries in self.statements:
                stmts_hetrogeneous.append(FinStatementsBase({date_item: stmt_timeseries[item]}))

            # inc_statement = self.income_statements[item]
            # inc_statements = IncomeStatements({date_item: inc_statement})
            # bs = self.balance_sheets[item]
            # b_sheets = BalanceSheets({date_item: bs})
        else:
            for stmt in self.statements:
                stmts_hetrogeneous.append(stmt[item])
            
            # inc_statements = self.income_statements[item]
            # b_sheets = self.balance_sheets[item]

        return FinancialStatements(stmts_hetrogeneous)
        # return FinancialStatements(inc_statements, b_sheets)

    def __dir__(self):
        normal_attrs = [
            # "income_statements",
            # "balance_sheets",
            # "capex",
            # "non_cash_expenses",
            # "fcf",
            "forecast",
            "forecasts",
            "forecast_assumptions",
            "dates",
            "copy",
        ]
        all_config_items = []
        for stmt in self.statements:
            all_config_items.extend(stmt.config.items)
        
        # all_config = (
        #     self.income_statements.config.items + self.balance_sheets.config.items
        # )
        item_attrs = [config_item.key for config_item in all_config_items]
        return normal_attrs + item_attrs

    # @property
    # def capex(self) -> pd.Series:
    #     return self.change("net_ppe") + self.dep

    # @property
    # def non_cash_expenses(self) -> pd.Series:
    #     # TODO [#5]: add stock-based compensation and use in non-cash expenses calculation
    #     return (
    #         self.dep
    #         + self.gain_on_sale_invest
    #         + self.gain_on_sale_asset
    #         + self.impairment
    #     )

    # @property
    # def fcf(self) -> pd.Series:
    #     return (
    #         self.net_income + self.non_cash_expenses - self.change("nwc") - self.capex
    #     )

    def forecast(self, **kwargs) -> "ForecastedFinancialStatements":
        """
        Run a forecast, returning forecasted financial statements

        :param kwargs: Attributes of :class:`finstmt.forecast.config.ForecastConfig`

        :Examples:

            >>> stmts.forecast(periods=2)

        """
        from finstmt.resolver.forecast import ForecastResolver

        if "bs_diff_max" in kwargs:
            bs_diff_max = kwargs["bs_diff_max"]
        else:
            bs_diff_max = ForecastConfig.bs_diff_max

        if "balance" in kwargs:
            balance = kwargs["balance"]
        else:
            balance = ForecastConfig.balance

        if "timeout" in kwargs:
            timeout = kwargs["timeout"]
        else:
            timeout = ForecastConfig.timeout

        self._validate_dates()

        all_forecast_dict = {}
        all_results = {}
        # for stmt in [self.income_statements, self.balance_sheets]:
        for stmt in self.statements:
            forecast_dict, results = stmt._forecast(self, **kwargs)
            all_forecast_dict.update(forecast_dict)
            all_results.update(results)

        resolver = ForecastResolver(
            self, all_forecast_dict, all_results, bs_diff_max, timeout, balance=balance
        )
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
        conf_items = []
        for stmts in self.statements:
            conf_items.extend(stmts.config.items)
        return conf_items
        # return self.income_statements.config.items + self.balance_sheets.config.items  # type: ignore

    @property
    def dates(self) -> List[pd.Timestamp]:
        self._validate_dates()
        return list(self.balance_sheets.statements.keys())

    def _validate_dates(self):
        for stmts1 in self.statements:
            for stmts2 in self.statements:
                stmts1_dates = set(stmts1.statements.keys())
                stmts2_dates = set(stmts2.statements.keys())
                if stmts1_dates != stmts2_dates:
                    stmts1_unique = stmts1_dates.difference(stmts2_dates)
                    stmts2_unique = stmts2_dates.difference(stmts1_dates)
                    message = "Got mismatching dates between historical statements. "
                    if stmts1_unique:
                        message += (
                            f"Balance sheet has {stmts1_unique} dates not in Income Statement. "
                        )
                    if stmts2_unique:
                        message += (
                            f"Income Statement has {stmts2_unique} dates not in Balance Sheet. "
                        )
                    raise MismatchingDatesException(message)

        # bs_dates = set(self.balance_sheets.statements.keys())
        # is_dates = set(self.income_statements.statements.keys())
        # if bs_dates != is_dates:
        #     bs_unique = bs_dates.difference(is_dates)
        #     is_unique = is_dates.difference(bs_dates)
        #     message = "Got mismatching dates between historical statements. "
        #     if bs_unique:
        #         message += (
        #             f"Balance sheet has {bs_unique} dates not in Income Statement. "
        #         )
        #     if is_unique:
        #         message += (
        #             f"Income Statement has {is_unique} dates not in Balance Sheet. "
        #         )
        #     raise MismatchingDatesException(message)

    def copy(self, **updates) -> Self:
        return dataclasses.replace(self, **updates)

    def __add__(self, other) -> Self:
        return self._combinator.add(self, other)

    def __radd__(self, other) -> Self:
        return self.__add__(other)

    def __sub__(self, other) -> Self:
        return self._combinator.subtract(self, other)

    def __rsub__(self, other) -> Self:
        return (-1 * self) + other

    def __mul__(self, other) -> Self:
        return self._combinator.multiply(self, other)

    def __rmul__(self, other) -> Self:
        return self.__mul__(other)

    def __truediv__(self, other) -> Self:
        return self._combinator.divide(self, other)

    def __rtruediv__(self, other):
        # TODO [#41]: implement right division for statements
        raise NotImplementedError(
            f"cannot divide type {type(other)} by type {type(self)}"
        )

    def __round__(self, n: Optional[int] = None) -> Self:
        new_statements = self.copy()
        for stmt in new_statements.statements:
            stmt = round(stmt, n) # type: ignore
        # new_statements.income_statements = round(new_statements.income_statements, n)  # type: ignore
        # new_statements.balance_sheets = round(new_statements.balance_sheets, n)  # type: ignore
        return new_statements


    @classmethod
    def from_df(
        cls,
        df: pd.DataFrame,
        statement_config_list: Optional[List[StatementConfig]] = None,
        disp_unextracted: bool = True,
    ):
        """
        DataFrame must have columns as dates and index as names of financial statement items
        """
        statements_dict = {}
        dates = list(df.columns)
        dates.sort(key=lambda t: pd.to_datetime(t))

        stmts = []
        for statment_config in statement_config_list:
            stmts.append(
                FinStatementsBase.from_df(
                    df,
                    statment_config.display_name,
                    statment_config.items_config_list,
                    disp_unextracted=False
                )
            )

        return cls(stmts)
