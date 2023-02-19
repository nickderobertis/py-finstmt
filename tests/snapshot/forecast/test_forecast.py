from typing import Final, Sequence

import matplotlib
from syrupy import SnapshotAssertion

from finstmt import FinancialStatements
from tests.snapshot.forecast.adjust_config import (
    FORECAST_ADJUSTS,
    AdjustDict,
    adjust_forecast_methods,
)
from tests.snapshot.forecast.snapshot_format import format_statement_for_snapshot

matplotlib.use("Agg")

FORECAST_KWARGS: Final = dict(periods=2)


def test_forecast_annual_stockrow_cat(
    annual_stockrow_stmts_cat: FinancialStatements, snapshot
):
    stmts = annual_stockrow_stmts_cat

    _forecast_test(
        stmts, snapshot, FORECAST_ADJUSTS["stockrow_cat"], exclude=("gross_ppe", "dep")
    )


def _forecast_test(
    stmts: FinancialStatements,
    snapshot: SnapshotAssertion,
    adjusts: AdjustDict,
    exclude: Sequence[str] = tuple(),
    **fcst_kwargs
):
    adjust_forecast_methods(stmts, adjusts)
    fcst = stmts.forecast(**{**FORECAST_KWARGS, **fcst_kwargs})
    assert format_statement_for_snapshot(fcst, exclude=exclude) == snapshot
