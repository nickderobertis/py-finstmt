from dataclasses import dataclass
from typing import Optional, Dict

from finstmt.findata.database import FinDataBase
from finstmt.inc.config import INCOME_STATEMENT_INPUT_ITEMS


@dataclass(unsafe_hash=True)
class IncomeStatementData(FinDataBase):
    revenue: Optional[float] = 0
    cogs: Optional[float] = 0
    sga: Optional[float] = 0
    int_exp: Optional[float] = 0
    tax_exp: Optional[float] = 0
    rd_exp: Optional[float] = 0
    dep_exp: Optional[float] = 0
    other_op_exp: Optional[float] = 0
    gain_on_sale_invest: Optional[float] = 0
    gain_on_sale_asset: Optional[float] = 0
    impairment: Optional[float] = 0

    op_exp: Optional[float] = None
    ebit: Optional[float] = None
    ebt: Optional[float] = None
    net_income: Optional[float] = None

    items_config = INCOME_STATEMENT_INPUT_ITEMS

    @property
    def gross_profit(self) -> Optional[float]:
        if self.revenue is None or self.cogs is None:
            return None
        return self.revenue - self.cogs

    @property
    def effective_tax_rate(self) -> float:
        if self.ebt is None:
            raise ValueError('cannot calculate effective tax rate as ebt is None')
        elif self.tax_exp is None:
            raise ValueError('cannot calculate effective tax rate is tax expense is None')
        return self.tax_exp / self.ebt

