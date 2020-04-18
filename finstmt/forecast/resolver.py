from typing import TYPE_CHECKING, List, Dict, Tuple

from sympy import Eq, sympify, IndexedBase, Idx
import pandas as pd
from sympy.logic.boolalg import BooleanFalse, BooleanTrue

from finstmt.forecast.main import Forecast
from finstmt.config_manage.data import _key_pct_of_key

if TYPE_CHECKING:
    from finstmt.combined.statements import FinancialStatements


class ForecastResolver:

    def __init__(self, stmts: 'FinancialStatements', forecast_dict: Dict[str, Forecast],
                 results: Dict[str, pd.Series]):
        self.stmts = stmts
        self.forecast_dict = forecast_dict
        self.results = results

    def get_solve_eqs_and_full_subs_dict(self) -> Tuple[List[Eq], Dict[IndexedBase, float]]:
        return get_solve_eqs_and_full_subs_dict(self.all_eqs, self.sympy_subs_dict)

    @property
    def t_indexed_eqs(self) -> List[Eq]:
        config_managers = [
            self.stmts.income_statements.statement_cls.items_config,
            self.stmts.balance_sheets.statement_cls.items_config,
        ]
        all_eqs = []
        for config_manage in config_managers:
            for config in config_manage:
                lhs = sympify(config.key + '[t]', locals=self.stmts.config.sympy_namespace)
                if config.expr_str is not None:
                    rhs = self.stmts.config.expr_for(config.key)
                elif config.forecast_config.pct_of is not None:
                    key_pct_of_key = _key_pct_of_key(config.key, config.forecast_config.pct_of)
                    rhs = sympify(f'{config.forecast_config.pct_of}[t] * {key_pct_of_key}[t]',
                                  locals=self.stmts.config.sympy_namespace)
                else:
                    rhs = lhs
                if not rhs == lhs:
                    eq = Eq(lhs, rhs)
                    all_eqs.append(eq)
        return all_eqs

    @property
    def all_eqs(self) -> List[Eq]:
        t_eqs = self.t_indexed_eqs
        out_eqs = []
        # Starting from 1 as 0 is last historical period, no need to calculate
        for period in range(1, self.num_periods):
            this_t_eqs = [eq.subs({self.t: period}) for eq in t_eqs]
            out_eqs.extend(this_t_eqs)
        return out_eqs

    @property
    def num_periods(self) -> int:
        # adding 1 because final existing period will be included as period 0
        return list(self.forecast_dict.values())[0].config.periods + 1

    @property
    def t(self) -> Idx:
        return self.stmts.config.sympy_namespace['t']

    @property
    def sympy_subs_dict(self) -> Dict[IndexedBase, float]:
        nper = self.num_periods
        subs_dict = {}
        for config in self.stmts.all_config_items:
            if config.forecast_config.pct_of:
                key = _key_pct_of_key(config.key, config.forecast_config.pct_of)
            else:
                key = config.key
            for period in range(nper):
                t_key = f'{key}[{period}]'
                lhs = sympify(t_key, locals=self.stmts.config.sympy_namespace)
                if period == 0:
                    # period 0 is last historical period, not forecasted period
                    try:
                        value = getattr(self.stmts, key).iloc[-1]
                    except AttributeError as e:
                        if '_pct_' in str(e):
                            # Got a percentage of item, only in forecasted results, skip
                            continue
                        else:
                            raise e
                else:
                    # period 1 or later, forecasted period, get from forecast results
                    # If it is a plug item, don't get forecasted values
                    if config.forecast_config.plug:
                        continue
                    try:
                        series = self.results[key]
                    except KeyError:
                        # Must not be a forecasted item, probably calculated item
                        continue
                    value = series.iloc[period - 1]
                subs_dict[lhs] = value
        return subs_dict

    @property
    def bs_balance_eqs(self) -> List[Eq]:
        eqs = []
        for period in range(1, self.num_periods):
            asset_key = f'total_assets[{period}]'
            lhs = sympify(asset_key, locals=self.stmts.config.sympy_namespace)
            liab_eq_key = f'total_liab_and_equity[{period}]'
            rhs = sympify(liab_eq_key, locals=self.stmts.config.sympy_namespace)
            eqs.append(Eq(lhs, rhs))
        return eqs


def get_solve_eqs_and_full_subs_dict(
    eqs_for_sub: List[Eq],
    subs_dict: Dict[IndexedBase, float]
) -> Tuple[List[Eq], Dict[IndexedBase, float]]:
    subbed_eqs = []
    subs_dict = subs_dict.copy()
    finished = False
    while not finished:
        next_eqs_to_sub = []
        for eq in eqs_for_sub:
            subbed = eq.xreplace(subs_dict)
            if isinstance(subbed, (BooleanFalse, BooleanTrue)):
                # Both lhs and rhs was subbed. This means it is a calculated item which was
                # added to the forecast because it is being used as pct_of in other items
                # Simply don't solve the equation again as the result is already in the subs dict
                continue
            elif subbed.rhs.free_symbols == set():
                # Equation is completely solved
                subbed_eqs.append(subbed)
                subs_dict[subbed.lhs] = subbed.rhs  # use it in other solutions
            else:
                # Equation still has remaining symbols, handle on next loop
                next_eqs_to_sub.append(subbed)
        if not next_eqs_to_sub:
            finished = True
        if eqs_for_sub == next_eqs_to_sub:
            # Went through a loop without any equations changed.
            # Not going to make any more progress, so exit without complete substitution
            finished = True
        eqs_for_sub = next_eqs_to_sub.copy()
    return eqs_for_sub, subs_dict