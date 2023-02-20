import operator
from typing import TYPE_CHECKING, Any, Callable, Protocol, Tuple, TypeVar, Union

from finstmt.findata.statementsbase import FinStatementsBase
from finstmt.forecast.main import Forecast

if TYPE_CHECKING:
    from finstmt.bs.main import BalanceSheets
    from finstmt.combined.statements import FinancialStatements
    from finstmt.inc.main import IncomeStatements

StatementT = TypeVar("StatementT", bound="FinancialStatements")
StatementCombiningItem = Union[FinStatementsBase, Forecast]
StatementCombiningItemT = TypeVar(
    "StatementCombiningItemT", bound=StatementCombiningItem
)


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
        statements = _combine_child_statements(statement, other, operator.add)
        return _new_statements(statement, other, *statements)

    def subtract(
        self, statement: "FinancialStatements", other: Any
    ) -> "FinancialStatements":
        statements = _combine_child_statements(statement, other, operator.sub)
        return _new_statements(statement, other, *statements)

    def multiply(
        self, statement: "FinancialStatements", other: Any
    ) -> "FinancialStatements":
        statements = _combine_child_statements(statement, other, operator.mul)
        return _new_statements(statement, other, *statements)

    def divide(
        self, statement: "FinancialStatements", other: Any
    ) -> "FinancialStatements":
        statements = _combine_child_statements(statement, other, operator.truediv)
        return _new_statements(statement, other, *statements)


def _combine_child_statements(
    statements: "FinancialStatements",
    other: Any,
    func: Callable[[StatementCombiningItemT, Any], StatementCombiningItemT],
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


def _new_statements(
    statements: "FinancialStatements",
    other_statements: "FinancialStatements",
    new_inc: "IncomeStatements",
    new_bs: "BalanceSheets",
) -> "FinancialStatements":
    from finstmt import FinancialStatements
    from finstmt.forecast.statements import ForecastedFinancialStatements

    if isinstance(statements, ForecastedFinancialStatements) and isinstance(
        other_statements, ForecastedFinancialStatements
    ):
        raise NotImplementedError(
            "not yet implemented to combine two forecasted statements"
        )
    if isinstance(statements, ForecastedFinancialStatements):
        return ForecastedFinancialStatements(
            new_inc,
            new_bs,
            calculate=statements.calculate,
            auto_adjust_config=statements.auto_adjust_config,
            forecasts=statements.forecasts,
        )
    if isinstance(other_statements, ForecastedFinancialStatements):
        return ForecastedFinancialStatements(
            new_inc,
            new_bs,
            calculate=statements.calculate,
            auto_adjust_config=statements.auto_adjust_config,
            forecasts=statements.forecasts,
        )

    return FinancialStatements(new_inc, new_bs)
