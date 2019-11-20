from typing import Dict, Any

from sympy import symbols, IndexedBase, Idx, Expr, sympify

from finstmt.exc import NotACalculatedItemException

class ConfigManagerBase:

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

    def expr_for(self, item_key: str) -> Expr:
        config = self.get(item_key)
        if config.expr_str is None:
            raise NotACalculatedItemException(item_key)
        expr = sympify(config.expr_str, locals=self.sympy_namespace)
        return expr

    def eq_subs_dict(self, values_dict: Dict[str, float], t_offset: int = 0) -> Dict[IndexedBase, float]:
        out_dict = {}
        t = self.sympy_namespace['t']
        for item_key, item_symbol in self.sympy_namespace.items():
            if item_key in values_dict:
                indexed_symbol = item_symbol.__getitem__(t + t_offset)  # eg cash[t] or cash[t-1]
                out_dict[indexed_symbol] = values_dict[item_key]
        return out_dict
