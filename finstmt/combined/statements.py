from dataclasses import dataclass

import pandas as pd

from finstmt import BalanceSheets, IncomeStatements


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

    def __dir__(self):
        normal_attrs = [
            'income_statements',
            'balance_sheets',
        ]
        all_config = self.income_statements.statement_cls.items_config + self.balance_sheets.statement_cls.items_config
        item_attrs = [config.key for config in all_config]
        return normal_attrs + item_attrs

    @property
    def capex(self) -> pd.Series:
        return self.change('ppe') # TODO: add depreciation when it's available

    @property
    def fcf(self) -> pd.Series:
        # TODO: add non-cash expenses when it's available
        return self.net_income - self.change('nwc') - self.capex
