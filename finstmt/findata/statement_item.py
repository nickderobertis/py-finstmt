from dataclasses import dataclass, field
from typing import Optional

import numpy as np
from sympy import Indexed, sympify

from finstmt.items.config import ItemConfig


@dataclass
class StatementItem:
    item_config: ItemConfig
    seed_value: Optional[float] = None
    calculated_value: Optional[np.float64] = field(init=False, default=None)

    def __post_init__(self) -> None:
        # If extracted and need to force positive, take absolute value
        if self.seed_value is None:
            return

        if self.item_config.force_positive:
            positive_value = abs(self.seed_value)
            self.seed_value = positive_value

    @property
    def value(self) -> Optional[np.float64]:
        # if specific value was provided, then return that even if it's a
        # calculated field
        if (self.seed_value is not None) and (not np.isnan(self.seed_value)):
            return np.float64(self.seed_value)

        if self.item_config.expr_str is None:
            return np.float64(0)

        return self.calculated_value

    def resolve_eq(self, date, finStmts):
        if (
            not self.item_config.expr_str
        ):  # if expression string is null or empty, don't do anything
            return

        ns_syms = finStmts.global_sympy_namespace
        sym_expr = sympify(self.item_config.expr_str, locals=ns_syms)
        sub_list = []
        t = ns_syms["t"]

        for sym in sym_expr.free_symbols:
            # free_symbols include everything from the provided namespace as
            #  well as all symbols in the expression
            # we will make an assumption that the symbols that we are actually
            #   interested in from the provided expresison string must have an
            #   index
            # we will skip any items in free_symbols that are not indexed
            if type(sym) is not Indexed:
                continue
            # get the series for the attribute
            series = getattr(finStmts, str(sym.base))

            # next we need to determine if the indexed symbol refers to the
            #   current period or a different period
            # We assume that there is only ONE index
            idx = sym.indices[0]
            if idx == t:
                offset = 0
            else:
                offset = idx.args[0]

            series_index_t0 = series.index.get_loc(date)
            series_index_with_offset = series_index_t0 + offset

            if series_index_with_offset < 0:
                self.calculated_value = None
                return

            date_with_offset = series.index[int(series_index_with_offset)]
            sub_value = series[date_with_offset]

            sub_list.append((sym, sub_value))

        result = np.float64(sym_expr.subs(sub_list))
        self.calculated_value = result
