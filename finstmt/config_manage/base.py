from typing import Dict, Any, List, Set

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

    def _calculated_item_determinant_keys(self, item_key: str) -> List[str]:
        determinant_keys: List[str] = []
        to_process_keys: List[str] = [item_key]
        i = -1
        while len(to_process_keys) > 0:
            i += 1
            process_key = to_process_keys.pop()
            if i != 0:
                # Add to determinants if not original key
                determinant_keys.append(process_key)
            try:
                expr = self.expr_for(process_key)
            except NotACalculatedItemException:
                continue
            new_keys = self._expr_to_keys(expr)
            to_process_keys.extend(new_keys)
        return determinant_keys

    def item_determinant_keys(self, item_key: str, include_pct_of: bool = True) -> List[str]:
        determinant_keys = self._calculated_item_determinant_keys(item_key)
        if include_pct_of:
            for item in self.items:
                # TODO: multiple passes through determinants may be necessary for complicated pct_of structures
                if item.key in determinant_keys and item.forecast_config.pct_of is not None:
                    pct_conf = self.get(item.forecast_config.pct_of)
                    if pct_conf.expr_str is None:
                        determinant_keys.append(item.forecast_config.pct_of)
                    else:
                        determinant_keys.extend(self._calculated_item_determinant_keys(pct_conf.key))
        return list(set(determinant_keys))

    @property
    def balance_groups(self) -> List[Set[ItemConfig]]:
        balance_sets: List[Set[str]] = []
        for item in self.items:
            if item.forecast_config.balance_with is not None:
                # Skip items already tracked
                item_tracked = False
                for bl in balance_sets:
                    # Balance item in a group which was already already found, skip
                    if item.key in bl:
                        item_tracked = True
                        break
                if item_tracked:
                    continue

                # Not already tracked, must be a new balance group
                balance_group: Set[str] = {item.key, item.forecast_config.balance_with}
                balance_with_conf = self.get(item.forecast_config.balance_with)
                if balance_with_conf.forecast_config.balance_with != item.key:
                    # This is part of a balance chain, e.g. a balanced with b, b balanced with c, c balanced with a
                    changed = True
                    while changed:
                        num_balanced = len(balance_group)
                        balance_group.add(balance_with_conf.forecast_config.balance_with)
                        new_num_balanced = len(balance_group)
                        changed = num_balanced != new_num_balanced
                        balance_with_conf = self.get(balance_with_conf.forecast_config.balance_with)

                balance_sets.append(balance_group)
        return balance_sets

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
