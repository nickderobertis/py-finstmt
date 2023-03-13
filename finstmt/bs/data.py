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
        _fields = [(item.key, numpy.float64, 0) for item in self.items_config_list]
        self.__class__ = make_dataclass(
            'finstmt.bs.data.BalanceSheetData', 
            fields=_fields, 
            bases=(FinDataBase, )
            )

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

        if key == "items_config":
            return object.__getattribute__(self, key)
        if key not in self.items_config.keys:
            return object.__getattribute__(self, key)

        expr_str = self.items_config.get(key).expr_str

        if expr_str is None:
            return object.__getattribute__(self, key)
        else:
            # print(f"Expression: {item_key} = {expr_str}")
            ns_syms = self.data.get('items_config').sympy_namespace
            sym_expr = sympify(expr_str, locals=ns_syms)
            sub_list = []
            t = ns_syms["t"]
            for ns_sym in ns_syms.values():
                if ns_sym == t:
                    continue
                if ns_sym[t] in sym_expr.free_symbols:
                    sub_list.append((ns_sym[t], self.data.get(str(ns_sym))))
            return sym_expr.subs(sub_list)
        

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
