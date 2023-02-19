from typing import Final

import matplotlib

from finstmt import FinancialStatements
from tests.snapshot.forecast.adjust_config import (
    FORECAST_ADJUSTS,
    adjust_forecast_methods,
)
from tests.snapshot.forecast.snapshot_format import format_statement_for_snapshot

matplotlib.use("Agg")

FORECAST_KWARGS: Final = dict(periods=2)


def test_forecast_annual_stockrow_cat(
    annual_stockrow_stmts_cat: FinancialStatements, snapshot
):
    stmts = annual_stockrow_stmts_cat

    adjust_forecast_methods(stmts, FORECAST_ADJUSTS["stockrow_cat"])
    fcst_kwargs = {**FORECAST_KWARGS}
    fcst = stmts.forecast(**fcst_kwargs)
    assert format_statement_for_snapshot(fcst, exclude=("gross_ppe", "dep")) == snapshot
