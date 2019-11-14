from copy import deepcopy
import warnings
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

    def __post_init__(self):
        for item in self.items_config:
            if item.force_positive and item.extract_names is not None:
                # If extracted and need to force positive, take absolute value
                value = getattr(self, item.key)
                if value is None:
                    continue
                positive_value = abs(value)
                setattr(self, item.key, positive_value)

    def _repr_html_(self):
        series = self.to_series()
        df = pd.DataFrame(series)
        return df.applymap(lambda x: f'${x:,.0f}' if not x == 0 else ' - ')._repr_html_()

    @classmethod
    def from_series(cls, series: pd.Series):
        for_lookup = deepcopy(series)
        standardize_names_in_series_index(for_lookup)
        data_dict = {}
        extracted_name_dict = {}
        for name in for_lookup.index:
            for item_config in cls.items_config:
                if item_config.extract_names is None:
                    # Not an extractable item, must be a calculated item
                    continue
                if name in item_config.extract_names:
                    # Got a match for series name to allowed names
                    if item_config.key in data_dict:
                        # Multiple matches for data item.
                        # First see if data is the same, then just skip
                        if for_lookup[name] == data_dict[item_config.key]:
                            continue
                        # Data is not the same, so take the one which is earliest in extract_names
                        current_match_idx = item_config.extract_names.index(name)
                        existing_match_idx = item_config.extract_names.index(extracted_name_dict[item_config.key])
                        current_match_is_preferred = current_match_idx < existing_match_idx
                        if current_match_is_preferred:
                            warnings.warn(f'Previously had {data_dict[item_config.key]} for {item_config.key} '
                                          f'extracted from {extracted_name_dict[item_config.key]}. Replacing with '
                                          f'{for_lookup[name]} from {name}')
                        else:
                            warnings.warn(f'Got {for_lookup[name]} for {item_config.key} from {name} but already '
                                          f'had {data_dict[item_config.key]} from '
                                          f'{extracted_name_dict[item_config.key]} which has higher priority, '
                                          f'keeping {data_dict[item_config.key]}')
                            continue
                    data_dict[item_config.key] = for_lookup[name]
                    extracted_name_dict[item_config.key] = name
        return cls(**data_dict)

    def to_series(self) -> pd.Series:
        data_dict = {}
        for item_config in self.items_config:
            data_dict[item_config.display_name] = getattr(self, item_config.key)
        return pd.Series(data_dict).fillna(0)