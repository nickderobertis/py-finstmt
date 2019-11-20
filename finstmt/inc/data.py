from dataclasses import dataclass
from typing import Optional, Dict

from sympy import IndexedBase

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

    prior_statement: Optional['FinDataBase'] = None
    items_config = INCOME_STATEMENT_INPUT_ITEMS

    def __post_init__(self):
        super().__post_init__()
        subs_dict = self.get_sympy_subs_dict()
        for config in self.items_config:
            item_value = getattr(self, config.key)
            if item_value is None and config.expr_str is not None:
                # Got a calculated item which has no value from the data, need to calculate
                expr = self.items_config.expr_for(config.key)
                eval_expr = expr.subs(subs_dict)
                setattr(self, config.key, float(eval_expr))
        # if self.op_exp is None:
        #     self.op_exp = self.rd_exp + self.dep_exp + self.sga + self.other_op_exp
        # if self.ebit is None:
        #     self.ebit = self.gross_profit - self.op_exp
        # if self.ebt is None:
        #     self.ebt = self.ebit - self.int_exp
        # if self.net_income is None:
        #     self.net_income = self.ebt - self.tax_exp

    @property
    def gross_profit(self) -> float:
        return self.revenue - self.cogs

    @property
    def effective_tax_rate(self) -> float:
        return self.tax_exp / self.ebt

    def get_sympy_subs_dict(self, t_offset: int = 0) -> Dict[IndexedBase, float]:
        subs_dict = self.items_config.eq_subs_dict(self.as_dict(), t_offset=t_offset)
        if self.prior_statement is not None:
            # Recursively look up prior statements to fill out historical values
            subs_dict.update(
                self.prior_statement.get_sympy_subs_dict(t_offset = t_offset - 1)
            )
        return subs_dict

