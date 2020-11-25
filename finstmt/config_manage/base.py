from typing import Dict, Any, List

from sympy import symbols, IndexedBase, Idx, Expr, sympify, Eq

from finstmt.exc import NotACalculatedItemException
from finstmt.items.config import ItemConfig


class ConfigManagerBase:

    def get(self, item_key: str) -> ItemConfig:
        """
        For internal use, get the config as well as the key of the financial statement type it belongs to
        """
        raise NotImplementedError

    def set(self, item_key: str, config: ItemConfig) -> None:
        """
        Set entire configuration for item by key. Needs to handle setting the value in each individual
        data config manager
        """
        raise NotImplementedError

    @property
    def sympy_namespace(self) -> Dict[str, IndexedBase]:
        """
        The sympy namespace containing all the variable definitions
        """
        raise NotImplementedError

    @property
    def items(self) -> List[ItemConfig]:
        """
        All the configuration items
        """
        raise NotImplementedError

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

    def eqs_involving(self, item_key: str) -> List[Eq]:
        ns = self.sympy_namespace
        item_sym = ns[item_key]
        t = ns['t']
        item_t = item_sym[t]
        eqs: List[Eq] = []
        for config in self.items:
            if config.expr_str is None:
                continue
            rhs = self.expr_for(config.key)
            if item_t in rhs.free_symbols:
                this_item_sym = ns[config.key]
                this_item_sym_t = this_item_sym[t]
                eq = Eq(this_item_sym_t, rhs)
                eqs.append(eq)

        return eqs

    def _expr_to_keys(self, expr: Expr) -> List[str]:
        ns = self.sympy_namespace
        t = ns['t']
        syms = expr.free_symbols
        keys: List[str] = []
        for key, key_expr in ns.items():
            if key == 't':
                continue
            key_expr_t = key_expr[t]
            if key_expr_t in syms:
                keys.append(key)
        return keys

    def eq_subs_dict(self, values_dict: Dict[str, float], t_offset: int = 0) -> Dict[IndexedBase, float]:
        out_dict = {}
        t = self.sympy_namespace['t']
        for item_key, item_symbol in self.sympy_namespace.items():
            if item_key in values_dict:
                indexed_symbol = item_symbol.__getitem__(t + t_offset)  # eg cash[t] or cash[t-1]
                out_dict[indexed_symbol] = values_dict[item_key]
        return out_dict
