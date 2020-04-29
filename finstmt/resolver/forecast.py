from dataclasses import dataclass
from typing import List, Dict, Tuple, Optional, Sequence

from scipy.optimize import minimize, OptimizeResult
from sympy import Eq, sympify, IndexedBase, Expr, solve, Indexed
import pandas as pd
import numpy as np
from sympy.core.numbers import NaN

from finstmt.config_manage.statements import StatementsConfigManager
from finstmt.exc import BalanceSheetNotBalancedException, MissingDataException, InvalidForecastEquationException
from finstmt.forecast.main import Forecast
from finstmt.config_manage.data import _key_pct_of_key
from finstmt.forecast.statements import ForecastedFinancialStatements
from finstmt.items.config import ItemConfig
from finstmt.logger import logger
from finstmt.combined.statements import FinancialStatements
from finstmt.resolver.base import ResolverBase

# TODO [#46]: clean up ForecastResolver
#
# `ForecastResolver` and associated logic is messy after reworking it multiple times.
# Need to remove unneeded code and restructure more logic into classes. `PlugResult`
# could handle more operations with the plugs, and the math could be more separated
# from the finance logic.
from finstmt.resolver.solve import PLUG_SCALE, solve_equations, sympy_dict_to_results_dict, _x_arr_to_plug_solutions, \
    _symbolic_to_matrix, _solve_eqs_with_plug_solutions, _get_indexed_symbols


class ForecastResolver(ResolverBase):

    def __init__(self, stmts: 'FinancialStatements', forecast_dict: Dict[str, Forecast],
                 results: Dict[str, pd.Series], bs_diff_max: float, balance: bool = True):
        self.forecast_dict = forecast_dict
        self.results = results
        self.bs_diff_max = bs_diff_max
        self.balance = balance

        if balance:
            self.exclude_plugs = True
        else:
            self.exclude_plugs = False

        super().__init__(stmts)

    def resolve_balance_sheet(self):
        logger.info('Balancing balance sheet')

        solutions_dict = self.subs_dict.copy()
        new_solutions = resolve_balance_sheet(
            self.plug_x0,
            self.solve_eqs,
            self.plug_keys,
            self.subs_dict,
            self.forecast_dates,
            self.stmts.config,
            self.stmts.config.sympy_namespace,
            self.bs_diff_max,
        )
        solutions_dict.update(new_solutions)

        return solutions_dict

    def to_statements(self) -> ForecastedFinancialStatements:
        if self.balance:
            solutions_dict = self.resolve_balance_sheet()
        else:
            if self.solve_eqs:
                solutions_dict = solve_equations(self.solve_eqs, self.subs_dict)
            else:
                solutions_dict = self.subs_dict

        new_results = sympy_dict_to_results_dict(
            solutions_dict, self.forecast_dates, self.stmts.all_config_items, t_offset=1
        )

        if self.balance:
            # Update forecast dict for plug values
            for config in self.plug_configs:
                self.forecast_dict[config.key].to_manual(use_levels=True, replacements=new_results[config.key].values)

        all_results = pd.concat(list(new_results.values()), axis=1).T
        inc_df = self.stmts.income_statements.__class__.from_df(
            all_results, self.stmts.income_statements.config.items, disp_unextracted=False
        )
        bs_df = self.stmts.balance_sheets.__class__.from_df(
            all_results, self.stmts.balance_sheets.config.items, disp_unextracted=False
        )

        # type ignore added because for some reason mypy is not picking up structure
        # correctly since it is a dataclass
        obj = ForecastedFinancialStatements(inc_df, bs_df, forecasts=self.forecast_dict, calculate=False)  # type: ignore
        return obj

    @property
    def t_indexed_eqs(self) -> List[Eq]:
        config_managers = [
            self.stmts.income_statements.config.items,
            self.stmts.balance_sheets.config.items,
        ]
        all_eqs = []
        for config_manage in config_managers:
            for config in config_manage:
                lhs = sympify(config.key + '[t]', locals=self.stmts.config.sympy_namespace)
                if config.expr_str is not None:
                    rhs = self.stmts.config.expr_for(config.key)
                elif config.forecast_config.pct_of is not None and config.forecast_config.make_forecast:
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

        all_hardcoded = _x_arr_to_plug_solutions(self.plug_x0, self.plug_keys, self.stmts.config.sympy_namespace)
        all_hardcoded.update(self.sympy_subs_dict)
        new_eqs = _get_equations_reformed_for_needed_solutions(out_eqs, all_hardcoded, self.stmts.config)

        return new_eqs

    @property
    def num_periods(self) -> int:
        # adding 1 because final existing period will be included as period 0
        return list(self.forecast_dict.values())[0].config.periods + 1

    @property
    def forecast_dates(self) -> pd.DatetimeIndex:
        return list(self.results.values())[0].index

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
                    if self.exclude_plugs and config.forecast_config.plug:
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

    @property
    def plug_keys(self) -> List[str]:
        return [config.key for config in self.plug_configs]

    @property
    def plug_x0(self) -> np.array:
        x_arrs = []
        plug_keys = []
        for config in self.plug_configs:
            x_arrs.append(self.results[config.key].values)
            plug_keys.append(config.key)
        x0 = np.concatenate(x_arrs) / PLUG_SCALE
        return x0


@dataclass
class PlugResult:
    res: Optional[np.array] = None


def resolve_balance_sheet(x0: np.ndarray, eqs: List[Eq], plug_keys: Sequence[str],
                          subs_dict: Dict[IndexedBase, float], forecast_dates: pd.DatetimeIndex,
                          config: StatementsConfigManager,
                          sympy_namespace: Dict[str, IndexedBase], bs_diff_max: float) -> Dict[IndexedBase, float]:
    plug_solutions = _x_arr_to_plug_solutions(x0, plug_keys, sympy_namespace)
    all_to_solve: Dict[IndexedBase, Expr] = {}
    for eq in eqs:
        expr = eq.rhs - eq.lhs
        if expr == NaN():
            raise InvalidForecastEquationException(f'got NaN forecast equation. LHS: {eq.lhs}, RHS: {eq.rhs}')
        if eq.lhs in all_to_solve:
            raise InvalidForecastEquationException(
                f'got multiple equations to solve for {eq.lhs}. Already had {all_to_solve[eq.lhs]}, now got {expr}'
            )
        all_to_solve[eq.lhs] = expr
    for sol_dict in [subs_dict, plug_solutions]:
        # Plug solutions second here so that they are at end of array
        for lhs, rhs in sol_dict.items():
            expr = rhs - lhs
            if expr == NaN():
                raise MissingDataException(f'got NaN for {lhs} but that is needed for resolving the forecast')
            if lhs in all_to_solve:
                existing_value = all_to_solve[lhs]
                if isinstance(existing_value, float):
                    had_message = f'forecast/plug value of {existing_value}'
                else:
                    had_message = f'equation of {existing_value}'
                raise InvalidForecastEquationException(
                    f'got forecast/plug value for {lhs} but already had an existing {had_message}, now got {expr}'
                )
            all_to_solve[lhs] = expr
    to_solve_for = list(all_to_solve.keys())
    solve_exprs = list(all_to_solve.values())
    _check_for_invalid_system_of_equations(eqs, subs_dict, plug_solutions, to_solve_for, solve_exprs)
    eq_arrs = _symbolic_to_matrix(solve_exprs, to_solve_for)

    result = PlugResult()
    res: Optional[OptimizeResult] = None
    try:
        res = minimize(
            _resolve_balance_sheet_check_diff,
            x0,
            args=(eq_arrs, forecast_dates, to_solve_for, bs_diff_max, result),
            bounds=[(0, None) for _ in range(len(x0))],  # all positive
            method='TNC',
            options=dict(
                maxCGit=0,
            )
        )
    except BalanceSheetBalancedException:
        pass
    if result.res is None:
        message: Optional[str]
        if res is not None:
            plug_solutions = _x_arr_to_plug_solutions(res.x, plug_keys, sympy_namespace)
            avg_error = (res.fun ** 2 / len(res.x)) ** 0.5
            message = (
                f'final solution {plug_solutions} still could not meet max difference of '
                f'${bs_diff_max:,.0f}. Average difference was ${avg_error:,.0f}.\nIf the make_forecast or plug '
                f'configuration for any items were changed, ensure that changes in {plug_keys} can flow through '
                f'to Total Assets and Total Liabilities and Equity. For example, if make_forecast=True for Total Debt '
                f'and make_forecast=False for ST Debt, then using LT debt as a plug will not work as ST debt will '
                f'go down when LT debt goes up.\nOtherwise, consider '
                f'passing bs_diff_max to .forecast at a value greater than {avg_error:,.0f}, or pass '
                f'balance=False to skip balancing entirely.'
            )
        else:
            message = None
        raise BalanceSheetNotBalancedException(message)
    plug_solutions = _x_arr_to_plug_solutions(result.res, plug_keys, sympy_namespace)
    solutions_dict = _solve_eqs_with_plug_solutions(
        eqs, plug_solutions, subs_dict, forecast_dates, config.items
    )
    return solutions_dict


def _resolve_balance_sheet_check_diff(x: np.ndarray, eq_arrs: Tuple[np.ndarray, np.ndarray],
                                      forecast_dates: pd.DatetimeIndex,
                                      solve_for: Sequence[IndexedBase],
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


class BalanceSheetBalancedException(Exception):
    pass


def _check_for_invalid_system_of_equations(eqs: List[Eq], subs_dict: Dict[IndexedBase, float],
                                           plug_solutions: Dict[IndexedBase, float],
                                           to_solve_for: List[IndexedBase], solve_exprs: List[Expr]):
    if len(to_solve_for) == len(solve_exprs):
        # Equations seem valid, just return
        return

    # Invalid equations, figure out why
    eq_lhs = {eq.lhs for eq in eqs}
    subs_lhs = {key for key in subs_dict}
    plugs_lhs = {key for key in plug_solutions}
    message = f'Got {len(to_solve_for)} items to solve for with {len(solve_exprs)} equations. '
    eq_subs_overlap = eq_lhs.intersection(subs_lhs)
    if eq_subs_overlap:
        message += f'Got {eq_subs_overlap} which overlap between the equations and the calculated values. '
    eq_plugs_overlap = eq_lhs.intersection(plugs_lhs)
    if eq_plugs_overlap:
        message += f'Got {eq_plugs_overlap} which overlap between the equations and the plug values. '
    subs_plugs_overlap = subs_lhs.intersection(plugs_lhs)
    if subs_plugs_overlap:
        message += f'Got {subs_plugs_overlap} which overlap between the calculated values and the plug values. '
    raise InvalidForecastEquationException(message)


def _get_equations_reformed_for_needed_solutions(eqs: Sequence[Eq], all_hardcoded: Dict[IndexedBase, float],
                                                 config: StatementsConfigManager) -> List[Eq]:
    new_eqs = []
    for eq in eqs:
        if eq.lhs in all_hardcoded:
            # Got a calculated item which has also been set with make_forecast=True or as plug=True
            # Solve the equation to see if there is another variable we can set as the lhs which
            # has make_forecast=False and plug=False
            selected_lhs: Optional[IndexedBase] = None
            for sym in _get_indexed_symbols(eq.rhs):
                if sym not in all_hardcoded:
                    selected_lhs = sym
            if selected_lhs is None:
                # Invalid forecast, need to display useful message to the user to fix it.
                # Need to get the original unsubbed equation, as possible variables the user could adjust might
                # have been substituted out of the equation
                key = str(eq.lhs.base)
                orig_expr = config.expr_for(key)
                orig_eq = Eq(eq.lhs, orig_expr)

                possible_fix_strs = []
                possible_symbols = _get_indexed_symbols(orig_eq)
                for sym in possible_symbols:
                    sym_key = str(sym.base)
                    fix_str = f'\tstmts.config.update("{sym_key}", ["forecast_config", "make_forecast"], False)\n\t' \
                              f'stmts.config.update("{sym_key}", ["forecast_config", "plug"], False)'
                    possible_fix_strs.append(fix_str)
                possible_fix_str = '\nor,\n'.join(possible_fix_strs)

                raise InvalidForecastEquationException(
                    f'{eq.lhs} has been set with make_forecast=True or plug=True and yet it is a calculated '
                    f'item. Tried to re-express {orig_eq} in terms of another variable which is not forecasted or '
                    f'plugged but they all are. Set one of {_get_indexed_symbols(orig_eq)} '
                    f'with make_forecast=False and plug=False.\n\nPossible fixes:\n{possible_fix_str}'
                )
            # Another variable in the original equation is not forecasted/plugged. Re-express the equation in
            # terms of that variable
            solution = solve(eq, selected_lhs)[0]
            new_eqs.append(Eq(selected_lhs, solution))
        else:
            new_eqs.append(eq)
    return new_eqs