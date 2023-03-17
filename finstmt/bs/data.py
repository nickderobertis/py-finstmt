from dataclasses import dataclass, make_dataclass, field, fields
from typing import Optional
from copy import deepcopy

from finstmt.bs.config import BALANCE_SHEET_INPUT_ITEMS
from finstmt.findata.database import FinDataBase

from typing import Dict, List, Optional, Sequence, Union, cast
from finstmt.config_manage.data import DataConfigManager
from finstmt.items.config import ItemConfig

import numpy
from sympy import sympify, symbols, Idx

@dataclass(unsafe_hash=True)
class BalanceSheetData(FinDataBase):

    t = symbols("t", cls=Idx)

    def __init__(self, *args, **kwargs):
        _fields = [(item.key, numpy.float64, field(default=0, repr=(False if item.key == "nwc" else True))) for item in self.items_config_list]
        sort_order = {
            "cash": 0,
            "st_invest": 1,
            "receivables": 2,
            "inventory": 3,
            "lt_invest": 4,
            "def_tax_st": 5,
            "other_current_assets": 6,
            "gross_ppe": 7,
            "dep": 8,
            "goodwill": 9,
            "def_tax_lt": 10,
            "other_lt_assets": 11,
            "payables": 12,
            "current_lt_debt": 13,
            "st_debt": 14,
            "lt_debt": 15,
            "deferred_rev": 16,
            "tax_liab_st": 17,
            "other_current_liab": 18,
            "tax_liab_lt": 19,
            "deposit_liab": 20,
            "other_lt_liab": 21,
            "common_stock": 22,
            "minority_interest": 23,
            "other_income": 24,
            "retained_earnings": 25,
            "cash_and_st_invest": 26,
            "total_current_assets": 27,
            "net_ppe": 28,
            "total_non_current_assets": 29,
            "total_assets": 30,
            "total_current_liab": 31,
            "total_debt": 32,
            "total_non_current_liab": 33,
            "total_liab": 34,
            "total_equity": 35,
            "total_liab_and_equity": 36,       
            "nwc": 37     
        }
        _fields.sort(key=lambda tup: sort_order[tup[0]])
        MyClass = make_dataclass(
            'BalanceSheetData', 
            fields=_fields, 
            bases=(FinDataBase, ),
            namespace={'nwc': lambda self: self.receivables + self.inventory - self.payables}
            )
        MyClass.__module__ = "finstmt.bs.data"
        self.__class__ = MyClass


        for key, value in kwargs.items():
            # print(f"{key}: {value}")
            setattr(self, key, value)

        self.items_config = DataConfigManager(deepcopy(self.items_config))

        for item in self.items_config:
            if item.force_positive and item.extract_names is not None:
                # If extracted and need to force positive, take absolute value
                value = getattr(self, item.key)
                if value is None:
                    continue
                positive_value = abs(value)
                setattr(self, item.key, positive_value)

    # Get item even if attribute exists
    def __getattribute__(self, key: str):
        # print("BalanceSheetData.__getattribute__", key)
        return object.__getattribute__(self, key)


    # cash: Optional[float] = 0
    # st_invest: Optional[float] = 0
    # receivables: Optional[float] = 0
    # inventory: Optional[float] = 0
    # lt_invest: Optional[float] = 0
    # def_tax_st: Optional[float] = 0
    # other_current_assets: Optional[float] = 0
    # gross_ppe: Optional[float] = 0
    # dep: Optional[float] = 0
    # goodwill: Optional[float] = 0
    # def_tax_lt: Optional[float] = 0
    # other_lt_assets: Optional[float] = 0
    # payables: Optional[float] = 0
    # current_lt_debt: Optional[float] = 0
    # st_debt: Optional[float] = 0
    # lt_debt: Optional[float] = 0
    # deferred_rev: Optional[float] = 0
    # tax_liab_st: Optional[float] = 0
    # other_current_liab: Optional[float] = 0
    # tax_liab_lt: Optional[float] = 0
    # deposit_liab: Optional[float] = 0
    # other_lt_liab: Optional[float] = 0
    # common_stock: Optional[float] = 0
    # minority_interest: Optional[float] = 0
    # other_income: Optional[float] = 0
    # retained_earnings: Optional[float] = 0

    # cash_and_st_invest: Optional[float] = None
    # total_current_assets: Optional[float] = None
    # net_ppe: Optional[float] = None
    # total_non_current_assets: Optional[float] = None
    # total_assets: Optional[float] = None
    # total_current_liab: Optional[float] = None
    # total_debt: Optional[float] = None
    # total_non_current_liab: Optional[float] = None
    # total_liab: Optional[float] = None
    # total_equity: Optional[float] = None
    # total_liab_and_equity: Optional[float] = None

    items_config_list = BALANCE_SHEET_INPUT_ITEMS

    # @property
    # def nwc(self):
    #     return self.receivables + self.inventory - self.payables