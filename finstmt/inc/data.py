from dataclasses import dataclass
from typing import Optional

from finstmt.findata.database import FinDataBase
from finstmt.inc.config import INCOME_STATEMENT_INPUT_ITEMS


@dataclass(unsafe_hash=True)
class IncomeStatementData(FinDataBase):
    revenue: float
    cogs: float
    sga: float
    int_exp: float
    tax_exp: float

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

    def __post_init__(self):
        super().__post_init__()
        if self.op_exp is None:
            self.op_exp = self.rd_exp + self.dep_exp + self.sga + self.other_op_exp
        if self.ebit is None:
            self.ebit = self.gross_profit - self.op_exp
        if self.ebt is None:
            self.ebt = self.ebit - self.int_exp
        if self.net_income is None:
            self.net_income = self.ebt - self.tax_exp

    @property
    def gross_profit(self) -> float:
        return self.revenue - self.cogs

    @property
    def effective_tax_rate(self) -> float:
        return self.tax_exp / self.ebt

