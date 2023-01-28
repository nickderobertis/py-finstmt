import warnings
from copy import deepcopy
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Sequence, Union, cast

import pandas as pd
from sympy import IndexedBase

from finstmt.clean.name import standardize_names_in_series_index
from finstmt.config_manage.data import DataConfigManager
from finstmt.exc import CouldNotParseException
from finstmt.items.config import ItemConfig


@dataclass
class FinDataBase:
    """
    Base class for financial statement data. Should not be used directly.
    """

    items_config: Union[List[ItemConfig], DataConfigManager]
    prior_statement: Optional["FinDataBase"] = None
    unextracted_names: List[str] = field(default_factory=lambda: [])

    def __init__(self, *args, **kwargs):
        raise NotImplementedError

    def __post_init__(self):
        self.items_config = DataConfigManager(deepcopy(self.items_config))
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
        return df.applymap(
            lambda x: f"${x:,.0f}" if not x == 0 else " - "
        )._repr_html_()

    @classmethod
    def from_series(
        cls,
        series: pd.Series,
        prior_statement: Optional["FinDataBase"] = None,
        items_config: Optional[Sequence[ItemConfig]] = None,
    ):
        if items_config is None:
            items_config = cast(Sequence[ItemConfig], cls.items_config)

        for_lookup = deepcopy(series)
        standardize_names_in_series_index(for_lookup)
        data_dict: Dict[str, Union[float, "FinDataBase"]] = {}
        extracted_name_dict: Dict[str, str] = {}
        original_name_dict: Dict[str, str] = {}
        unextracted_names: List[str] = []

        if prior_statement is not None:
            data_dict["prior_statement"] = prior_statement

        for i, name in enumerate(for_lookup.index):
            orig_name = series.index[i]
            for item_config in items_config:
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
                        existing_match_idx = item_config.extract_names.index(
                            extracted_name_dict[item_config.key]
                        )
                        current_match_is_preferred = (
                            current_match_idx < existing_match_idx
                        )
                        if current_match_is_preferred:
                            warnings.warn(
                                f"Previously had {item_config.key} "
                                f'extracted from "{original_name_dict[item_config.key]}". Replacing with '
                                f'value from "{orig_name}"'
                            )
                        else:
                            warnings.warn(
                                f'Found {item_config.key} from "{orig_name}" but already '
                                f"had extracted from "
                                f'"{original_name_dict[item_config.key]}" which has higher priority, '
                                f'keeping value from "{original_name_dict[item_config.key]}"'
                            )
                            continue
                    data_dict[item_config.key] = for_lookup[name]
                    extracted_name_dict[item_config.key] = name
                    original_name_dict[item_config.key] = orig_name
            if name not in extracted_name_dict.values():
                unextracted_names.append(orig_name)
        if not data_dict:
            raise CouldNotParseException(
                "Passed Series did not have any statement items in the index. "
                "Got index:",
                series.index,
            )
        return cls(
            **data_dict, items_config=items_config, unextracted_names=unextracted_names
        )

    def to_series(self) -> pd.Series:
        data_dict = {}
        for item_config in self.items_config:
            data_dict[item_config.display_name] = getattr(self, item_config.key)
        return pd.Series(data_dict).fillna(0)

    def as_dict(self) -> Dict[str, float]:
        remove_keys = ["items_config"]

        all_dict = deepcopy(self.__dict__)
        [all_dict.pop(key) for key in remove_keys]
        return all_dict

    def get_sympy_subs_dict(self, t_offset: int = 0) -> Dict[IndexedBase, float]:
        subs_dict = self.items_config.eq_subs_dict(self.as_dict(), t_offset=t_offset)  # type: ignore
        if self.prior_statement is not None:
            # Recursively look up prior statements to fill out historical values
            subs_dict.update(
                self.prior_statement.get_sympy_subs_dict(t_offset=t_offset - 1)
            )
        return subs_dict
