from dataclasses import dataclass
from typing import Optional

from finstmt.bs.config import BALANCE_SHEET_INPUT_ITEMS
from finstmt.findata.database import FinDataBase


@dataclass(unsafe_hash=True)
class BalanceSheetData(FinDataBase):
    cash: Optional[float] = 0
    st_invest: Optional[float] = 0
    receivables: Optional[float] = 0
    inventory: Optional[float] = 0
    lt_invest: Optional[float] = 0
    def_tax_st: Optional[float] = 0
    other_current_assets: Optional[float] = 0
    gross_ppe: Optional[float] = 0
    dep: Optional[float] = 0
    goodwill: Optional[float] = 0
    def_tax_lt: Optional[float] = 0
    other_lt_assets: Optional[float] = 0
    payables: Optional[float] = 0
    current_lt_debt: Optional[float] = 0
    st_debt: Optional[float] = 0
    lt_debt: Optional[float] = 0
    deferred_rev: Optional[float] = 0
    tax_liab_st: Optional[float] = 0
    other_current_liab: Optional[float] = 0
    tax_liab_lt: Optional[float] = 0
    deposit_liab: Optional[float] = 0
    other_lt_liab: Optional[float] = 0
    common_stock: Optional[float] = 0
    minority_interest: Optional[float] = 0
    other_income: Optional[float] = 0
    retained_earnings: Optional[float] = 0

    cash_and_st_invest: Optional[float] = None
    total_current_assets: Optional[float] = None
    net_ppe: Optional[float] = None
    total_non_current_assets: Optional[float] = None
    total_assets: Optional[float] = None
    total_current_liab: Optional[float] = None
    total_debt: Optional[float] = None
    total_non_current_liab: Optional[float] = None
    total_liab: Optional[float] = None
    total_equity: Optional[float] = None
    total_liab_and_equity: Optional[float] = None

    items_config = BALANCE_SHEET_INPUT_ITEMS

    @property
    def nwc(self):
        return self.receivables + self.inventory - self.payables
