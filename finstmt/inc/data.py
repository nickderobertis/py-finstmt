from copy import deepcopy
from dataclasses import dataclass
from typing import Optional

import pandas as pd

from finstmt.clean.name import standardize_names_in_series_index
from finstmt.inc.config import ALLOWED_NAMES


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
            for data_attr, allowed_values in ALLOWED_NAMES.items():
                if name in allowed_values:
                    # Got a match for series name to allowed names
                    if data_attr in data_dict:
                        raise ValueError(f'got multiple data items for {data_attr}. Was already set to '
                                         f'{data_dict[data_attr]} and now trying to also add {name}')
                    data_dict[data_attr] = for_lookup[name]
        return cls(**data_dict)

