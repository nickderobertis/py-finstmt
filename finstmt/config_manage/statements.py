from dataclasses import dataclass
from typing import Dict, Tuple

from sympy import IndexedBase

from finstmt.config_manage.base import ConfigManagerBase
from finstmt.config_manage.statement import StatementConfigManager
from finstmt.exc import NoSuchItemException
from finstmt.items.config import ItemConfig


@dataclass
class StatementsConfigManager(ConfigManagerBase):
    """
    Main configuration interface. Handles all of the configuration for a set of financial statements.
    """
    config_managers: Dict[str, StatementConfigManager]

    def get(self, item_key: str) -> ItemConfig:
        """
        Get entire configuration for item by key
        """
        config, _ = self._get(item_key)
        return config

    def _get(self, item_key: str) -> Tuple[ItemConfig, str]:
        """
        For internal use, get the config as well as the key of the financial statement type it belongs to
        """
        for fin_statement_type, manager in self.config_managers.items():
            try:
                return manager.get(item_key), fin_statement_type
            except NoSuchItemException:
                continue
        raise NoSuchItemException(item_key)

    def set(self, item_key: str, config: ItemConfig):
        """
        Set entire configuration for item by key
        """
        orig_config, fin_statement_key = self._get(item_key)
        self.config_managers[fin_statement_key].set(item_key, config)

    @property
    def sympy_namespace(self) -> Dict[str, IndexedBase]:
        ns_dict = {}
        for cfg_mgr in self.config_managers.values():
            ns_dict.update(cfg_mgr.sympy_namespace)
        return ns_dict
