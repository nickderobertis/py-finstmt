from dataclasses import dataclass
from typing import Sequence, Dict, Any

from sympy import symbols, IndexedBase, Idx

from finstmt.items.config import ItemConfig


@dataclass
class StatementConfigManager:
    configs: Sequence[ItemConfig]

    def __post_init__(self):
        self.configs = list(self.configs)

    def __getitem__(self, item):
        return self.configs[item]

    def get(self, item_key: str) -> ItemConfig:
        """
        Get entire configuration for item by key
        """
        return self.config_dict[item_key]

    def set(self, item_key: str, config: ItemConfig):
        """
        Set entire configuration for item by key
        """
        orig_config = self.get(item_key)
        config_idx = self.configs.index(orig_config)
        self.configs[config_idx] = config

    def get_value(self, item_key: str, config_key: str) -> Any:
        """
        Get a particular configuration for a particular item
        """
        config = self.get(item_key)
        return getattr(config, config_key)

    def set_value(self, item_key: str, config_key: str, value: Any):
        """
        Set a particular configuration for a particular item
        """
        orig_config = self.get(item_key)
        setattr(orig_config, config_key, value)
        self.set(item_key, orig_config)

    # TODO: make next two not properties, but recalculate any time config changes
    @property
    def config_dict(self) -> Dict[str, ItemConfig]:
        return {config.key: config for config in self.configs}

    @property
    def sympy_namespace(self) -> Dict[str, IndexedBase]:
        t = symbols('t', cls=Idx)
        ns_dict = {'t': t}
        for config in self.configs:
            expr = IndexedBase(config.key)
            ns_dict.update({config.key: expr})
        return ns_dict

