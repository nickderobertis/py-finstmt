from copy import deepcopy
from dataclasses import dataclass, field, make_dataclass

import numpy
from sympy import Idx, symbols

from finstmt.config_manage.data import DataConfigManager
from finstmt.findata.database import FinDataBase
from finstmt.inc.config import INCOME_STATEMENT_INPUT_ITEMS


@dataclass(unsafe_hash=True)
class IncomeStatementData(FinDataBase):
    t = symbols("t", cls=Idx)

    def __init__(self, *args, **kwargs):
        _fields = [
            (
                item.key,
                numpy.float64,
                field(default=0, repr=item.show_on_statement),
            )
            for item in self.items_config_list
        ]
        sort_order = {
            "revenue": 0,
            "cogs": 1,
            "gross_profit": 2,
            "sga": 3,
            "int_exp": 4,
            "tax_exp": 5,
            "rd_exp": 6,
            "dep_exp": 7,
            "other_op_exp": 8,
            "gain_on_sale_invest": 9,
            "gain_on_sale_asset": 10,
            "impairment": 11,
            "op_exp": 12,
            "ebit": 13,
            "ebt": 14,
            "net_income": 15,
        }
        _fields.sort(key=lambda tup: sort_order[tup[0]])
        MyClass = make_dataclass(
            "IncomeStatementData", fields=_fields, bases=(FinDataBase,)
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

    ###### THIS BREAKS THE DYNAMIC DATACLASS
    # def __setattr__(self, item_key, value):
    #     self.data[item_key] = value

    # items_config = INCOME_STATEMENT_INPUT_ITEMS
    items_config_list = INCOME_STATEMENT_INPUT_ITEMS

    # @property
    # def effective_tax_rate(self) -> float:
    #     if self.ebt is None:
    #         raise ValueError("cannot calculate effective tax rate as ebt is None")
    #     elif self.tax_exp is None:
    #         raise ValueError(
    #             "cannot calculate effective tax rate is tax expense is None"
    #         )
    #     return self.tax_exp / self.ebt
