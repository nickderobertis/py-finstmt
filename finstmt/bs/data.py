from dataclasses import dataclass
from typing import Optional

from finstmt.bs.config import BALANCE_SHEET_INPUT_ITEMS
from finstmt.findata.database import FinDataBase


@dataclass(unsafe_hash=True)
class BalanceSheetData(FinDataBase):
    cash: float
    st_invest: float
    receivables: float
    inventory: float
    ppe: float  # TODO: better handling for depreciation
    goodwill: float
    lt_invest: float
    tax_assets: float
    payables: float
    st_debt: float
    lt_debt: float
    # TODO: next four items should be optional, but not calculated
    deferred_rev: float
    tax_liab: float
    deposit_liab: float
    other_income: float
    retained_earnings: float


    total_current_assets: Optional[float] = None
    total_non_current_assets: Optional[float] = None
    total_assets: Optional[float] = None
    total_current_liab: Optional[float] = None
    total_debt: Optional[float] = None
    total_non_current_liab: Optional[float] = None
    total_liab: Optional[float] = None
    total_equity: Optional[float] = None


    items_config = BALANCE_SHEET_INPUT_ITEMS

    def __post_init__(self):
        if self.total_current_assets is None:
            self.total_current_assets = self.cash_and_st_invest + self.receivables + self.inventory  # TODO: check
        if self.total_non_current_assets is None:
            self.total_non_current_assets = self.ppe + self.goodwill + self.lt_invest + self.tax_assets
        if self.total_assets is None:
            self.total_assets = self.total_current_assets + self.total_non_current_assets
        if self.total_current_liab is None:
            self.total_current_liabilities = self.payables + self.st_debt
        if self.total_debt is None:
            self.total_debt = self.st_debt + self.lt_debt
        if self.total_non_current_liab is None:
            self.total_non_current_liab = self.lt_debt + self.deferred_rev + self.tax_liab + self.deposit_liab
        if self.total_liab is None:
            self.total_liab = self.total_non_current_liab + self.total_current_liab
        if self.total_equity is None:
            # TODO: common stock value not in stockrow data
            self.total_equity = self.other_income + self.retained_earnings

    @property
    def cash_and_st_invest(self):
        return self.cash + self.st_invest

    @property
    def nwc(self):
        return self.receivables + self.inventory - self.payables
