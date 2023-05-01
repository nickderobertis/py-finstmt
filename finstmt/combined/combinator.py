import operator
from typing import TYPE_CHECKING, Any, Callable, Dict, List, Protocol, Tuple, TypeVar

from typing_extensions import TypeGuard

if TYPE_CHECKING:
    from finstmt.bs.main import BalanceSheets
    from finstmt.combined.statements import FinancialStatements
    from finstmt.forecast.main import Forecast
    from finstmt.forecast.statements import ForecastedFinancialStatements
    from finstmt.inc.main import IncomeStatements

T = TypeVar("T")
StatementT = TypeVar("StatementT", bound="FinancialStatements")


class StatementsCombinator(Protocol[StatementT]):
    def add(self, statement: StatementT, other: Any) -> StatementT:
        ...

    def subtract(self, statement: StatementT, other: Any) -> StatementT:
        ...

    def multiply(self, statement: StatementT, other: Any) -> StatementT:
        ...

    def divide(self, statement: StatementT, other: Any) -> StatementT:
        ...


class FinancialStatementsCombinator(StatementsCombinator["FinancialStatements"]):
    def add(
        self, statement: "FinancialStatements", other: Any
    ) -> "FinancialStatements":
        statements = _apply_to_child_statements(
            statement, other, operator.add
        )
        # income_statements, balance_sheets = _apply_to_child_statements(
        #     statement, other, operator.add
        # )
        # return statement.copy(
        #     income_statements=income_statements, balance_sheets=balance_sheets
        # )
        return statement.copy(
            statements=statements
        )

    def subtract(
        self, statement: "FinancialStatements", other: Any
    ) -> "FinancialStatements":
        income_statements, balance_sheets = _apply_to_child_statements(
            statement, other, operator.sub
        )
        return statement.copy(
            income_statements=income_statements, balance_sheets=balance_sheets
        )

    def multiply(
        self, statement: "FinancialStatements", other: Any
    ) -> "FinancialStatements":
        income_statements, balance_sheets = _apply_to_child_statements(
            statement, other, operator.mul
        )
        return statement.copy(
            income_statements=income_statements, balance_sheets=balance_sheets
        )

    def divide(
        self, statement: "FinancialStatements", other: Any
    ) -> "FinancialStatements":
        income_statements, balance_sheets = _apply_to_child_statements(
            statement, other, operator.truediv
        )
        return statement.copy(
            income_statements=income_statements, balance_sheets=balance_sheets
        )


class ForecastedFinancialStatementsCombinator(
    StatementsCombinator["ForecastedFinancialStatements"]
):
    def add(
        self, statement: "ForecastedFinancialStatements", other: Any
    ) -> "ForecastedFinancialStatements":
        # income_statements, balance_sheets = _apply_to_child_statements(
        #     statement, other, operator.add
        # )
        statements = _apply_to_child_statements(
            statement, other, operator.add
        )
        # forecasts = _apply_to_forecasts(statement.forecasts, other, operator.add)
        forecasts = _apply_to_forecasts(statement.forecasts, other, operator.add)
        # return statement.copy(
        #     income_statements=income_statements,
        #     balance_sheets=balance_sheets,
        #     forecasts=forecasts,
        # )
        return statement.copy(
            statements=statements,
            forecasts=forecasts,
        )

    def subtract(
        self, statement: "ForecastedFinancialStatements", other: Any
    ) -> "ForecastedFinancialStatements":
        income_statements, balance_sheets = _apply_to_child_statements(
            statement, other, operator.sub
        )
        forecasts = _apply_to_forecasts(statement.forecasts, other, operator.sub)
        return statement.copy(
            income_statements=income_statements,
            balance_sheets=balance_sheets,
            forecasts=forecasts,
        )

    def multiply(
        self, statement: "ForecastedFinancialStatements", other: Any
    ) -> "ForecastedFinancialStatements":
        income_statements, balance_sheets = _apply_to_child_statements(
            statement, other, operator.mul
        )
        forecasts = _apply_to_forecasts(statement.forecasts, other, operator.mul)
        return statement.copy(
            income_statements=income_statements,
            balance_sheets=balance_sheets,
            forecasts=forecasts,
        )

    def divide(
        self, statement: "ForecastedFinancialStatements", other: Any
    ) -> "ForecastedFinancialStatements":
        income_statements, balance_sheets = _apply_to_child_statements(
            statement, other, operator.truediv
        )
        forecasts = _apply_to_forecasts(statement.forecasts, other, operator.truediv)
        return statement.copy(
            income_statements=income_statements,
            balance_sheets=balance_sheets,
            forecasts=forecasts,
        )


def _apply_to_child_statements(
    statements: "FinancialStatements",
    other: Any,
    func: Callable[[Any, Any], Any],
# ) -> Tuple["IncomeStatements", "BalanceSheets"]:
) -> List["FinStatementBase"]:
    from finstmt import FinancialStatements

    if isinstance(other, (float, int)):
        # new_inc = func(statements.income_statements, other)
        # new_bs = func(statements.balance_sheets, other)
        new_stmts = []
        for (left, right) in zip(statements.statements, other):
            new_stmt = func(left, right)
            new_stmts.append()
    elif isinstance(other, FinancialStatements):
        # new_inc = func(statements.income_statements, other.income_statements)
        # new_bs = func(statements.balance_sheets, other.balance_sheets)
        new_stmts = []
        for (left, right) in zip(statements.statements, other.statements):
            new_stmt = func(left, right)
            new_stmts.append(new_stmt)
    else:
        raise NotImplementedError(
            f"cannot {func.__name__} type {type(statements)} to type {type(other)}"
        )

    # return new_inc, new_bs
    return new_stmts


def _apply_to_forecasts(
    forecasts: Dict[str, "Forecast"],
    other: Any,
    func: Callable[["Forecast", Any], "Forecast"],
) -> Dict[str, "Forecast"]:
    if isinstance(other, (float, int)):
        return {k: func(v, other) for k, v in forecasts.items()}
    elif _is_forecasted_financial_statements(other):
        return {k: func(v, other.forecasts[k]) for k, v in forecasts.items()}
    else:
        raise NotImplementedError(
            f"cannot {func.__name__} type {type(forecasts)} to type {type(other)}"
        )


def _is_forecasted_financial_statements(
    obj: Any,
) -> TypeGuard["ForecastedFinancialStatements"]:
    return hasattr(obj, "forecasts")
