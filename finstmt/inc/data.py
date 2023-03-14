from dataclasses import dataclass, make_dataclass, field, fields
from typing import Optional, Dict
from copy import deepcopy

from finstmt.findata.database import FinDataBase
from finstmt.inc.config import INCOME_STATEMENT_INPUT_ITEMS
from finstmt.exc import NoSuchItemException
from finstmt.config_manage.data import DataConfigManager
import numpy
from sympy import sympify, symbols, Idx

from typing import Dict, List, Optional, Sequence, Union, cast
from finstmt.config_manage.data import DataConfigManager
from finstmt.items.config import ItemConfig

@dataclass(unsafe_hash=True)
class IncomeStatementData(FinDataBase):

    t = symbols("t", cls=Idx)

    def __init__(self, *args, **kwargs):
        _fields = [(item.key, numpy.float64, field(default=0, repr=(False if item.key == "gross_profit" else True))) for item in self.items_config_list]
        MyClass = make_dataclass(
            'IncomeStatementData', 
            fields=_fields, 
            bases=(FinDataBase, )
            )
        MyClass.__module__ = "finstmt.inc.data"
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
        # print("IncomeStatementData.__getattribute__", key)
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
        

    # # Get item if attribute doesn't exist
    # def __getattr__(self, item_key: str):
    #     """
    #     Get the Income Statement Value for a given key
    #     """
    #     try:
    #         print("IncomeStatementData.__getattribute__", item_key)
    #         if item_key == "items_config":
    #             return object.__getattribute__(self, item_key) # self[item_key]
            
    #         if item_key not in self.items_config.keys:
    #             return getattr(self, item_key) # self[item_key]
                            
    #         expr_str = self.items_config.get(item_key).expr_str

    #         if expr_str is None:
    #             return getattr(self, item_key) # self[item_key]
    #         else:
    #             # print(f"Expression: {item_key} = {expr_str}")
    #             ns_syms = self.items_config.sympy_namespace
    #             sym_expr = sympify(expr_str, locals=ns_syms)
    #             sub_list = []
    #             t = ns_syms["t"]
    #             for ns_sym in ns_syms.values():
    #                 if ns_sym == t:
    #                     continue
    #                 if ns_sym[t] in sym_expr.free_symbols:
    #                     sub_list.append((ns_sym[t], object.__getattribute__(self, str(ns_sym))))
    #             return sym_expr.subs(sub_list)
    #     except NoSuchItemException:
    #         raise AttributeError(item_key)

    # def __dir__(self):
    #     return list(self.data.keys()) + ["gross_profit"]

    ###### THIS BREAKS THE DYNAMIC DATACLASS
    # def __setattr__(self, item_key, value):
    #     self.data[item_key] = value

    # items_config = INCOME_STATEMENT_INPUT_ITEMS
    items_config_list = INCOME_STATEMENT_INPUT_ITEMS

    # revenue: Optional[float] = 0
    # cogs: Optional[float] = 0
    # sga: Optional[float] = 0
    # int_exp: Optional[float] = 0
    # tax_exp: Optional[float] = 0
    # rd_exp: Optional[float] = 0
    # dep_exp: Optional[float] = 0
    # other_op_exp: Optional[float] = 0
    # gain_on_sale_invest: Optional[float] = 0
    # gain_on_sale_asset: Optional[float] = 0
    # impairment: Optional[float] = 0

    # op_exp: Optional[float] = None
    # ebit: Optional[float] = None
    # ebt: Optional[float] = None
    # net_income: Optional[float] = None


    # @property
    # def gross_profit(self) -> Optional[float]:
    #     if self.revenue is None or self.cogs is None:
    #         return None
    #     return self.revenue - self.cogs

    # @property
    # def effective_tax_rate(self) -> float:
    #     if self.ebt is None:
    #         raise ValueError("cannot calculate effective tax rate as ebt is None")
    #     elif self.tax_exp is None:
    #         raise ValueError(
    #             "cannot calculate effective tax rate is tax expense is None"
    #         )
    #     return self.tax_exp / self.ebt

