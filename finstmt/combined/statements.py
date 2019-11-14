from dataclasses import dataclass

from finstmt import BalanceSheets, IncomeStatements


@dataclass
class FinancialStatements:
    income_statements: IncomeStatements
    balance_sheets: BalanceSheets

    def _repr_html_(self):
        return f"""
        <h2>Income Statement</h2>
        {self.income_statements._repr_html_()}
        <h2>Balance Sheet</h2>
        {self.balance_sheets._repr_html_()}
        """

    def __getattr__(self, item):
        inc_items = [config.key for config in self.income_statements.statement_cls.items_config]
        bs_items = [config.key for config in self.balance_sheets.statement_cls.items_config]
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