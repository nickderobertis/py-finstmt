from dataclasses import dataclass
from typing import TYPE_CHECKING, List, Dict, Tuple, Optional, Sequence

from scipy.optimize import minimize
from sympy import Eq, sympify, IndexedBase, Idx, linsolve, Expr, nonlinsolve, solve, Symbol, expand
import pandas as pd
import numpy as np
from sympy.core.numbers import NaN
from sympy.logic.boolalg import BooleanFalse, BooleanTrue

from finstmt.exc import BalanceSheetNotBalancedException, MissingDataException, InvalidForecastEquationException
from finstmt.forecast.main import Forecast
from finstmt.config_manage.data import _key_pct_of_key
from finstmt.forecast.statements import ForecastedFinancialStatements
from finstmt.items.config import ItemConfig
from finstmt.logger import logger

if TYPE_CHECKING:
    from finstmt.combined.statements import FinancialStatements

PLUG_SCALE = 1e11


class ForecastResolver:
    solve_eqs: Optional[List[Eq]] = None
    subs_dict: Optional[Dict[IndexedBase, float]] = None

    def __init__(self, stmts: 'FinancialStatements', forecast_dict: Dict[str, Forecast],
                 results: Dict[str, pd.Series], bs_diff_max: float):
        self.stmts = stmts
        self.forecast_dict = forecast_dict
        self.results = results
        self.bs_diff_max = bs_diff_max

        self.set_solve_eqs_and_full_subs_dict()

    def set_solve_eqs_and_full_subs_dict(self):
        self.solve_eqs, self.subs_dict = get_solve_eqs_and_full_subs_dict(self.all_eqs, self.sympy_subs_dict)

    def resolve_balance_sheet(self):
        logger.info('Balancing balance sheet')
        x_arrs = []
        plug_keys = []
        for config in self.plug_configs:
            x_arrs.append(self.results[config.key].values)
            plug_keys.append(config.key)
        x0 = np.concatenate(x_arrs) / PLUG_SCALE

        solutions_dict = self.subs_dict.copy()
        new_solutions = resolve_balance_sheet(
            x0,
            self.solve_eqs,
            plug_keys,
            self.subs_dict,
            self.forecast_dates,
            self.stmts.all_config_items,
            self.stmts.config.sympy_namespace,
            self.bs_diff_max,
        )
        solutions_dict.update(new_solutions)

        return solutions_dict

    def to_statements(self) -> ForecastedFinancialStatements:
        solutions_dict = self.resolve_balance_sheet()
        new_results = sympy_dict_to_results_dict(solutions_dict, self.forecast_dates, self.stmts.all_config_items)

        all_results = pd.concat(list(new_results.values()), axis=1).T
        inc_df = self.stmts.income_statements.__class__.from_df(all_results, self.stmts.income_statements.config.items)
        bs_df = self.stmts.balance_sheets.__class__.from_df(all_results, self.stmts.balance_sheets.config.items)

        # type ignore added because for some reason mypy is not picking up structure
        # correctly since it is a dataclass
        obj = ForecastedFinancialStatements(inc_df, bs_df, self.forecast_dict)  # type: ignore
        return obj

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
    def forecast_dates(self) -> pd.DatetimeIndex:
        return list(self.results.values())[0].index

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

    @property
    def plug_configs(self) -> List[ItemConfig]:
        return [conf for conf in self.stmts.all_config_items if conf.forecast_config.plug]


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
            subbed = Eq(eq.lhs, eq.rhs.xreplace(subs_dict))
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


@dataclass
class PlugResult:
    res: Optional[np.array] = None


def sympy_dict_to_results_dict(
    s_dict: Dict[IndexedBase, float],
    forecast_dates: pd.DatetimeIndex,
    item_configs: List[ItemConfig],
) -> Dict[str, pd.Series]:
    item_config_dict: Dict[str, ItemConfig] = {config.key: config for config in item_configs}
    new_results = {}
    for expr in s_dict:
        key = str(expr.base)
        try:
            config = item_config_dict[key]
        except KeyError:
            # Must be pct of item, don't need in final results
            continue
        new_results[key] = pd.Series(index=forecast_dates, dtype='float', name=config.primary_name)
    for expr, val in s_dict.items():
        key = str(expr.base)
        t = int(expr.indices[0]) - 1
        if t < 0:
            # Don't need to store historical results
            continue
        if key not in new_results:
            # Pct of item, skip it, don't need in final results
            continue
        new_results[key].iloc[t] = val
    return new_results


def results_dict_to_sympy_dict(results_dict: Dict[str, pd.Series],
                               sympy_namespace: Dict[str, Expr]) -> Dict[IndexedBase, float]:
    out_dict = {}
    for key, series in results_dict.items():
        arr = series.values
        for i, val in enumerate(arr):
            t_str = f'{key}[{i + 1}]'
            lhs = sympify(t_str, locals=sympy_namespace)
            out_dict[lhs] = val
    return out_dict


def solve_equations(solve_eqs: List[Eq], subs_dict: Dict[IndexedBase, float], substitute: bool = True,
                    round_results: bool = True):
    solutions_dict = subs_dict.copy()

    if substitute:
        solve_eqs, solutions_dict = get_solve_eqs_and_full_subs_dict(solve_eqs, solutions_dict)
    solve_exprs = []
    to_solve_for = []
    for eq in solve_eqs:
        solve_exprs.append(eq.rhs - eq.lhs)
        to_solve_for.append(eq.lhs)
    to_solve_for = list(set(to_solve_for))

    res_set = numpy_solve(solve_exprs, to_solve_for)
    if not res_set:
        raise ValueError('could not solve equations')
    solutions_dict.update(res_set)

    return solutions_dict


def resolve_balance_sheet(x0: np.ndarray, eqs: List[Eq], plug_keys: Sequence[str],
                          subs_dict: Dict[IndexedBase, float], forecast_dates: pd.DatetimeIndex,
                          item_configs: List[ItemConfig],
                          sympy_namespace: Dict[str, IndexedBase], bs_diff_max: float) -> Dict[IndexedBase, float]:
    plug_solutions = _x_arr_to_plug_solutions(x0, plug_keys, sympy_namespace)
    solve_exprs = []
    to_solve_for = []
    for eq in eqs:
        expr = eq.rhs - eq.lhs
        if expr == NaN():
            raise InvalidForecastEquationException(f'got NaN forecast equation. LHS: {eq.lhs}, RHS: {eq.rhs}')
        solve_exprs.append(expr)
        to_solve_for.append(eq.lhs)
    for sol_dict in [subs_dict, plug_solutions]:
        # Plug solutions second here so that they are at end of array
        for lhs, rhs in sol_dict.items():
            expr = rhs - lhs
            if expr == NaN():
                raise MissingDataException(f'got NaN for {lhs} but that is needed for resolving the forecast')
            solve_exprs.append(expr)
            to_solve_for.append(lhs)
    to_solve_for = list(set(to_solve_for))
    eq_arrs = _symbolic_to_matrix(solve_exprs, to_solve_for)

    result = PlugResult()
    res = None
    try:
        res = minimize(
            _resolve_balance_sheet_check_diff,
            x0,
            args=(eq_arrs, forecast_dates, item_configs, to_solve_for, bs_diff_max, result),
            bounds=[(0, None) for _ in range(len(x0))],  # all positive
            method='TNC',
            options=dict(
                maxCGit=0,
            )
        )
    except BalanceSheetBalancedException:
        pass
    if result.res is None:
        if res is not None:
            message = f'final solution {res.x * PLUG_SCALE} still could not meet max difference of {bs_diff_max}'
        else:
            message = None
        raise BalanceSheetNotBalancedException(message)
    plug_solutions = _x_arr_to_plug_solutions(result.res, plug_keys, sympy_namespace)
    solutions_dict = _solve_eqs_with_plug_solutions(
        eqs, plug_solutions, subs_dict, forecast_dates, item_configs
    )
    return solutions_dict


def _resolve_balance_sheet_check_diff(x: np.ndarray, eq_arrs: Tuple[np.ndarray, np.ndarray],
                                      forecast_dates: pd.DatetimeIndex,
                                      item_configs: List[ItemConfig], solve_for: Sequence[IndexedBase],
                                      bs_diff_max: float, res: PlugResult):
    A_arr, b_arr = eq_arrs
    b_arr[-len(x):] = -x * PLUG_SCALE  # plug solutions with new X values
    sol_arr = np.linalg.solve(A_arr, b_arr)
    solutions_dict = {}
    assets_arr = np.zeros(len(forecast_dates))
    le_arr = np.zeros(len(forecast_dates))
    for value, var in zip(sol_arr, solve_for):
        solutions_dict[var] = value
        key = str(var.base)
        if key == 'total_assets':
            t = int(var.indices[0]) - 1
            if t > 0:
                assets_arr[t] = value
        elif key == 'total_liab_and_equity':
            t = int(var.indices[0]) - 1
            if t > 0:
                le_arr[t] = value

    diff = abs(assets_arr - le_arr).astype(float)
    norm = np.linalg.norm(diff)
    logger.debug(f'x: {x * PLUG_SCALE}, norm: {norm}')
    desired_norm = np.linalg.norm([bs_diff_max] * len(diff))
    if norm <= desired_norm:
        res.res = x
        raise BalanceSheetBalancedException(x)
    return norm


def _solve_eqs_with_plug_solutions(eqs: List[Eq], plug_solutions: Dict[IndexedBase, float],
                                   subs_dict: Dict[IndexedBase, float], forecast_dates: pd.DatetimeIndex,
                                   item_configs: List[ItemConfig]) -> Dict[IndexedBase, float]:
    subs_dict = subs_dict.copy()
    subs_dict.update(plug_solutions)
    sub_eqs = [Eq(lhs, rhs) for lhs, rhs in subs_dict.items()]
    solutions_dict = solve_equations(eqs + sub_eqs, {}, substitute=False)

    return solutions_dict


def _x_arr_to_plug_solutions(x: np.ndarray, plug_keys: Sequence[str],
                             sympy_namespace: Dict[str, IndexedBase]) -> Dict[IndexedBase, float]:
    x_arrs = np.split(x * PLUG_SCALE, len(plug_keys))
    plug_dict = {key: pd.Series(x_arrs[i]) for i, key in enumerate(plug_keys)}
    plug_solutions = results_dict_to_sympy_dict(plug_dict, sympy_namespace)
    return plug_solutions


def _symbolic_to_matrix(exprs: Sequence[Expr], variables: Sequence[Symbol]):

    """
    Expr should be in the format of eq.lhs - eq.rhs

    Assuming that there exists numeric matrix A such that equation F = 0
    is equivalent to linear equation Ax = b, this function returns
    tuple (A, b)
    """
    A = []
    b = []
    for expr in exprs:
        coeffs = expand(expr).as_coefficients_dict()
        A.append([float(coeffs[x]) for x in variables])
        b.append(-float(coeffs[1]))
    return np.array(A), np.array(b)


def numpy_solve(exprs: Sequence[Expr], variables: Sequence[Symbol]):
    a_arr, b_arr = _symbolic_to_matrix(exprs, variables)
    x = np.linalg.solve(a_arr, b_arr)
    solution_dict = {var: x[i] for i, var in enumerate(variables)}
    return solution_dict


class BalanceSheetBalancedException(Exception):
    pass



