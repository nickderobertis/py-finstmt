from copy import deepcopy
from dataclasses import dataclass, field, make_dataclass

import numpy

from finstmt.bs.config import BALANCE_SHEET_INPUT_ITEMS
from finstmt.config_manage.data import DataConfigManager
from finstmt.findata.database import FinDataBase


@dataclass(unsafe_hash=True)
class BalanceSheetData(FinDataBase):
    def __init__(self, *args, **kwargs):
        _fields = [
            (
                item.key,
                numpy.float64,
                field(default=0, repr=item.show_on_statement),
            )
            for item in self.items_config_list
        ]
        MyClass = make_dataclass(
            "BalanceSheetData",
            fields=_fields,
            bases=(FinDataBase,),
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
        return object.__getattribute__(self, key)

    items_config_list = BALANCE_SHEET_INPUT_ITEMS
