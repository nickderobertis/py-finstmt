from dataclasses import dataclass
from typing import Optional

from finstmt.findata.database import FinDataBase
from finstmt.inc.config import INCOME_STATEMENT_INPUT_ITEMS


@dataclass(unsafe_hash=True)
class IncomeStatementData(FinDataBase):
    revenue: float
    cogs: float
    rd_exp: float
    sga: float
    int_exp: float
    tax_exp: float
    # TODO: there's no depreciation in the stockrow data

    op_exp: Optional[float] = None
    items_config = INCOME_STATEMENT_INPUT_ITEMS

    def __post_init__(self):
        if self.op_exp is None:
            self.op_exp = self.rd_exp + self.sga

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

