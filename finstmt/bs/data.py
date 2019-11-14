from dataclasses import dataclass
from typing import Optional

from finstmt.bs.config import BALANCE_SHEET_INPUT_ITEMS
from finstmt.findata.database import FinDataBase


@dataclass(unsafe_hash=True)
class BalanceSheetData(FinDataBase):
    cash: float
    receivables: float
    inventory: float
    lt_invest: float
    payables: float
    st_debt: float
    lt_debt: float
    retained_earnings: float

    st_invest: Optional[float] = 0
    def_tax_st: Optional[float] = 0
    other_current_assets: Optional[float] = 0
    gross_ppe: Optional[float] = 0
    dep: Optional[float] = 0
    goodwill: Optional[float] = 0
    def_tax_lt: Optional[float] = 0
    other_lt_assets: Optional[float] = 0
    current_lt_debt: Optional[float] = 0
    deferred_rev: Optional[float] = 0
    tax_liab_st: Optional[float] = 0
    other_current_liab: Optional[float] = 0
    tax_liab_lt: Optional[float] = 0
    deposit_liab: Optional[float] = 0
    other_lt_liab: Optional[float] = 0
    common_stock: Optional[float] = 0
    minority_interest: Optional[float] = 0
    other_income: Optional[float] = 0

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

    def __post_init__(self):
        super().__post_init__()
        if self.cash_and_st_invest is None:
            self.cash_and_st_invest = self.cash + self.st_invest
        if self.total_current_assets is None:
            self.total_current_assets = self.cash_and_st_invest + self.receivables + self.inventory + \
                                        self.def_tax_st + self.other_current_assets
        if self.net_ppe is None:
            self.net_ppe = self.gross_ppe - self.dep
        if self.total_non_current_assets is None:
            self.total_non_current_assets = self.net_ppe + self.goodwill + self.lt_invest + self.def_tax_lt + \
                                            self.other_lt_assets
        if self.total_assets is None:
            self.total_assets = self.total_current_assets + self.total_non_current_assets
        if self.total_current_liab is None:
            self.total_current_liabilities = self.payables + self.st_debt + self.tax_liab_st + self.current_lt_debt + \
                                             self.other_current_liab
        if self.total_debt is None:
            self.total_debt = self.st_debt + self.lt_debt
        if self.total_non_current_liab is None:
            self.total_non_current_liab = self.lt_debt + self.deferred_rev + self.tax_liab_lt + self.deposit_liab + \
                                          self.other_lt_liab
        if self.total_liab is None:
            self.total_liab = self.total_non_current_liab + self.total_current_liab
        if self.total_equity is None:
            self.total_equity = self.other_income + self.retained_earnings + self.common_stock + self.minority_interest
        if self.total_liab_and_equity is None:
            self.total_liab_and_equity = self.total_liab + self.total_equity

    @property
    def nwc(self):
        return self.receivables + self.inventory - self.payables
