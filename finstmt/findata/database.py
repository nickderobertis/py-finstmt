from copy import deepcopy
from dataclasses import dataclass
from typing import Optional, List

import pandas as pd

from finstmt.clean.name import standardize_names_in_series_index
from finstmt.items.config import ItemConfig


class FinDataBase:
    """
    Base class for financial statement data. Should not be used directly.
    """
    items_config: List[ItemConfig]

    @classmethod
    def from_series(cls, series: pd.Series):
        for_lookup = deepcopy(series)
        standardize_names_in_series_index(for_lookup)
        data_dict = {}
        for name in for_lookup.index:
            for item_config in cls.items_config:
                if item_config.extract_names is None:
                    # Not an extractable item, must be a calculated item
                    continue
                if name in item_config.extract_names:
                    # Got a match for series name to allowed names
                    if item_config.key in data_dict:
                        raise ValueError(f'got multiple data items for {item_config.key}. Was already set to '
                                         f'{data_dict[item_config.key]} and now trying to also add {name}')
                    data_dict[item_config.key] = for_lookup[name]
        return cls(**data_dict)

    def to_series(self) -> pd.Series:
        data_dict = {}
        for item_config in self.items_config:
            data_dict[item_config.display_name] = getattr(self, item_config.key)
        return pd.Series(data_dict)