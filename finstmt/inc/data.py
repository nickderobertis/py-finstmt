from copy import deepcopy
from dataclasses import dataclass
from typing import Optional

import pandas as pd

from finstmt.clean.name import standardize_names_in_series_index
from finstmt.inc.config import INCOME_STATEMENT_INPUT_ITEMS


@dataclass(unsafe_hash=True)
class IncomeStatementData:
    revenue: float
    cogs: float
    rd_exp: float
    sga: float
    int_exp: float
    tax_exp: float

    op_exp: Optional[float] = None

    def __post_init__(self):
        if self.op_exp is None:
            self.op_exp = self.rd_exp + self.sga  # TODO: check

    @property
    def gross_profit(self) -> float:
        return self.revenue - self.cogs

    @property
    def ebit(self) -> float:
        return self.gross_profit - self.op_exp

    @property
    def ebt(self) -> float:
        return self.ebit - self.int_exp

    @property
    def net_income(self) -> float:
        return self.ebt - self.tax_exp

    @property
    def effective_tax_rate(self) -> float:
        return self.tax_exp / self.ebt

    @classmethod
    def from_series(cls, series: pd.Series):
        for_lookup = deepcopy(series)
        standardize_names_in_series_index(for_lookup)
        data_dict = {}
        for name in for_lookup.index:
            for item_config in INCOME_STATEMENT_INPUT_ITEMS:
                if item_config.extract_names is None:
                    # Not an extractable item, must be a calculated item
                    continue
                if name in item_config.extract_names:
                    # Got a match for series name to allowed names
                    if item_config.key in data_dict:
                        raise ValueError(f'got multiple data items for {item_config.key}. Was already set to '
                                         f'{data_dict[item_config.key]} and now trying to also add {name}')
                    data_dict[item_config.key] = for_lookup[name]
        return cls(**data_dict)

    def to_series(self) -> pd.Series:
        data_dict = {}
        for item_config in INCOME_STATEMENT_INPUT_ITEMS:
            data_dict[item_config.display_name] = getattr(self, item_config.key)
        return pd.Series(data_dict)
