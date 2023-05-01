import json
import warnings
from copy import deepcopy
from typing import TYPE_CHECKING, Dict, List, Optional, cast

import numpy as np
import pandas as pd
from sympy import IndexedBase, sympify

from finstmt.clean.name import standardize_names_in_series_index
from finstmt.config_manage.data import DataConfigManager
from finstmt.exc import CouldNotParseException
from finstmt.findata.statement_item import StatementItem

if TYPE_CHECKING:
    from finstmt.combined.statements import FinancialStatements


class PeriodFinancialData:
    """
    Base class for financial statement data. Should not be used directly.
    """

    config_manager: DataConfigManager
    prior_statement: Optional["PeriodFinancialData"]
    unextracted_names: List[str]
    statement_items: Dict[str, StatementItem]
    global_sympy_namespace: Dict[str, IndexedBase]

    # TODO: Set this via user config
    maximum_display_verbosity = 1

    def __init__(
        self,
        data_dict: Dict[str, float],
        config_manager: DataConfigManager,
        unextracted_names: List[str],
        global_sympy_namespace: Dict[str, IndexedBase],
        prior_statement: Optional["PeriodFinancialData"] = None,
    ):
        self.config_manager = DataConfigManager(deepcopy(config_manager.configs))
        self.prior_statement = prior_statement
        self.unextracted_names = unextracted_names
        self.global_sympy_namespace = global_sympy_namespace

        self.statement_items = {}
        for item in self.config_manager:
            self.statement_items[item.key] = StatementItem(
                item_config=deepcopy(item),
                value=data_dict.get(item.key, None),
            )

    # after all statement items have been established do a second loop and solve any equations that we can
    # repeat this step on the higher levels
    def resolve_expressions(self, date, finStmts: "FinancialStatements"):
        for statement_item in self.statement_items.values():
            statement_item.resolve_eq(date, finStmts)

    def _repr_html_(self):
        series = self.to_series()
        df = pd.DataFrame(series)
        return df.applymap(
            lambda x: f"${x:,.0f}" if not x == 0 else " - "
        )._repr_html_()

    def __repr__(self) -> str:
        statement_items: dict = cast(dict, self.statement_items)
        results = {}
        for k, v in statement_items.items():
            val = v.get_value()
            # Some properties, e.g., nwc and effective tax rate, may be associated with a statements, but we don't
            # necessarily want to display it on the print-out
            if (val != 0) and (
                v.item_config.display_verbosity <= self.maximum_display_verbosity
            ):
                results[k] = val

        return json.dumps(str(results), indent=2)

    def __dir__(self):
        normal_attrs = [
            "config_manager",
            "prior_statement",
            "unextracted_names",
            "statement_items",
            "from_series",
            "to_series",
            "dict",
        ]
        return normal_attrs + list(self.statement_items.keys())

    @classmethod
    def from_series(
        cls,
        series: pd.Series,
        config_manager: DataConfigManager,
        global_sympy_namespace: Dict[str, IndexedBase],
        prior_statement: Optional["PeriodFinancialData"] = None,
    ):
        for_lookup = deepcopy(series)
        standardize_names_in_series_index(for_lookup)
        data_dict: Dict[str, float] = {}
        extracted_name_dict: Dict[str, str] = {}
        original_name_dict: Dict[str, str] = {}
        unextracted_names: List[str] = []

        for i, name in enumerate(for_lookup.index):
            orig_name = series.index[i]
            for item_config in config_manager:
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
                        # Data is not the same, so take the one which is
                        # earliest in extract_names
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
        return cls(
            data_dict=data_dict,
            config_manager=config_manager,
            unextracted_names=unextracted_names,
            global_sympy_namespace=global_sympy_namespace,
            prior_statement=prior_statement

        )

    # Return a series of all the items in the current period
    # Any formulas that refer to other items from this statement should be solved by the time thie formula returns
    def to_series(self, index_as_display_name=True) -> pd.Series:
        data_dict = {}
        for item_config in self.config_manager:
            if index_as_display_name:
                data_dict[item_config.display_name] = getattr(self, item_config.key)
            else:
                data_dict[item_config.extract_names[0] if item_config.extract_names is not None else item_config.key] = getattr(self, item_config.key)

        return pd.Series(data_dict).fillna(0)

    def __getattr__(self, key: str):
        try:
            statement_item = self.statement_items[key]
        except KeyError:
            raise AttributeError(key)
        # return np.float64(self.resolve_eq(statement_item.get_value()))
        return statement_item.get_value()
    
