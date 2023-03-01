from dataclasses import dataclass
from typing import Optional, Dict
from copy import deepcopy

from finstmt.findata.database import FinDataBase
from finstmt.inc.config import INCOME_STATEMENT_INPUT_ITEMS
from finstmt.exc import NoSuchItemException
from finstmt.config_manage.data import DataConfigManager

from sympy import sympify, symbols, Idx

@dataclass(unsafe_hash=True)
class IncomeStatementData(FinDataBase):
    data = {}
    t = symbols("t", cls=Idx)

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            # print(f"{key}: {value}")
            setattr(self, key, value)

        self.items_config = DataConfigManager(deepcopy(self.items_config))

        for item in self.items_config:
            # Check if item wasn't in initial data load but it is in the config. If so, set it to 0
            if item.key not in self.data.keys(): # and item.expr_str is None:
                setattr(self, item.key, 0)
            if item.force_positive and item.extract_names is not None:
                # If extracted and need to force positive, take absolute value
                value = getattr(self, item.key)
                if value is None:
                    continue
                positive_value = abs(value)
                setattr(self, item.key, positive_value)
            
    # def __post_init__(self):
    #     print("IncomeStatementData __post_init__ 1", type(self.items_config))
    #     super().__post_init__()
    #     print("IncomeStatementData __post_init__ 2", type(self.items_config))
    #     return  
    

    def __getattr__(self, item_key: str):
        """
        Get the Income Statement Value for a given key
        """
        try:
            if item_key == "items_config":
                return self.data.get(item_key)
            
            if item_key not in self.items_config.keys:
                return self.data.get(item_key)
                            
            expr_str = self.items_config.get(item_key).expr_str

            if expr_str is None:
                return self.data.get(item_key)
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
        except NoSuchItemException:
            raise AttributeError(item_key)

    def __dir__(self):
        return list(self.data.keys()) + ["gross_profit"]

    def __setattr__(self, item_key, value):
        self.data[item_key] = value

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


    @property
    def gross_profit(self) -> Optional[float]:
        if self.revenue is None or self.cogs is None:
            return None
        return self.revenue - self.cogs

    @property
    def effective_tax_rate(self) -> float:
        if self.ebt is None:
            raise ValueError("cannot calculate effective tax rate as ebt is None")
        elif self.tax_exp is None:
            raise ValueError(
                "cannot calculate effective tax rate is tax expense is None"
            )
        return self.tax_exp / self.ebt

