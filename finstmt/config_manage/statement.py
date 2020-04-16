from dataclasses import dataclass
from typing import Dict, Tuple, List

from sympy import IndexedBase
import pandas as pd

from finstmt.config_manage.base import ConfigManagerBase
from finstmt.config_manage.data import DataConfigManager
from finstmt.exc import NoSuchItemException
from finstmt.items.config import ItemConfig


@dataclass
class StatementConfigManager(ConfigManagerBase):
    """
    Used for entire single financial statement, e.g. income statement or balance sheet, with multiple dates in the
    statement.
    """
    config_managers: Dict[pd.Timestamp, DataConfigManager]

    def get(self, item_key: str) -> ItemConfig:
        """
        For internal use, get the config as well as the key of the financial statement type it belongs to
        """
        for manager in self.config_managers.values():
            try:
                return manager.get(item_key)
            except KeyError:
                continue
        raise NoSuchItemException(item_key)

    def set(self, item_key: str, config: ItemConfig) -> None:
        """
        Set entire configuration for item by key. Needs to handle setting the value in each individual
        data config manager
        """
        for manager in self.config_managers.values():
            manager.set(item_key, config)

    @property
    def sympy_namespace(self) -> Dict[str, IndexedBase]:
        for manager in self.config_managers.values():
            # All should be identical, so first is enough
            return manager.sympy_namespace
        raise ValueError('no managers, could not get sympy_namespace')

    @property
    def keys(self) -> List[str]:
        all_keys = set()
        for manager in self.config_managers.values():
            all_keys.update(manager.keys)
        return list(all_keys)
