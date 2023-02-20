import operator
from typing import Any, Callable, Protocol, TYPE_CHECKING, Tuple, TypeVar

from finstmt.findata.statementsbase import FinStatementsBase

if TYPE_CHECKING:
    from finstmt.bs.main import BalanceSheets
    from finstmt.combined.statements import FinancialStatements
    from finstmt.forecast.statements import ForecastedFinancialStatements
    from finstmt.inc.main import IncomeStatements

T = TypeVar("T")
StatementT = TypeVar("StatementT", bound="FinancialStatements")
FinStatementsBaseT = TypeVar("FinStatementsBaseT", bound=FinStatementsBase)


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
        income_statements, balance_sheets = _apply_to_child_statements(
            statement, other, operator.add
        )
        return statement.copy(
            income_statements=income_statements, balance_sheets=balance_sheets
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
        income_statements, balance_sheets = _apply_to_child_statements(
            statement, other, operator.add
        )
        return statement.copy(
            income_statements=income_statements, balance_sheets=balance_sheets
        )

    def subtract(
        self, statement: "ForecastedFinancialStatements", other: Any
    ) -> "ForecastedFinancialStatements":
        income_statements, balance_sheets = _apply_to_child_statements(
            statement, other, operator.sub
        )
        return statement.copy(
            income_statements=income_statements, balance_sheets=balance_sheets
        )

    def multiply(
        self, statement: "ForecastedFinancialStatements", other: Any
    ) -> "ForecastedFinancialStatements":
        income_statements, balance_sheets = _apply_to_child_statements(
            statement, other, operator.mul
        )
        return statement.copy(
            income_statements=income_statements, balance_sheets=balance_sheets
        )

    def divide(
        self, statement: "ForecastedFinancialStatements", other: Any
    ) -> "ForecastedFinancialStatements":
        income_statements, balance_sheets = _apply_to_child_statements(
            statement, other, operator.truediv
        )
        return statement.copy(
            income_statements=income_statements, balance_sheets=balance_sheets
        )


def _apply_to_child_statements(
    statements: "FinancialStatements",
    other: T,
    func: Callable[[FinStatementsBaseT, T], FinStatementsBaseT],
) -> Tuple["IncomeStatements", "BalanceSheets"]:
    from finstmt import FinancialStatements

    if isinstance(other, (float, int)):
        new_inc = func(statements.income_statements, other)
        new_bs = func(statements.balance_sheets, other)
    elif isinstance(other, FinancialStatements):
        new_inc = func(statements.income_statements, other.income_statements)
        new_bs = func(statements.balance_sheets, other.balance_sheets)
    else:
        raise NotImplementedError(
            f"cannot {func.__name__} type {type(statements)} to type {type(other)}"
        )

    return new_inc, new_bs
