import sys
from pathlib import Path
from typing import Final, Sequence

import matplotlib
from _pytest.fixtures import FixtureRequest
from syrupy import SnapshotAssertion

from finstmt import FinancialStatements
from tests.integration.config import GENERATE_TEST_DATA
from tests.snapshot.forecast.adjust_config import (
    FORECAST_ADJUSTS,
    AdjustDict,
    adjust_forecast_methods,
)
from tests.snapshot.forecast.snapshot_format import format_statement_for_snapshot

matplotlib.use("Agg")

FORECAST_KWARGS: Final = dict(periods=2)

pdf_path = Path(__file__).parent / "__snapshots__" / "test_forecast_pdfs"
pdf_path.mkdir(parents=True, exist_ok=True)


def test_forecast_annual_stockrow_cat(
    annual_stockrow_stmts_cat: FinancialStatements, snapshot, request: FixtureRequest
):
    stmts = annual_stockrow_stmts_cat

    _forecast_test(
        stmts,
        snapshot,
        request,
        FORECAST_ADJUSTS["stockrow_cat"],
        exclude=("gross_ppe", "dep"),
    )


def _forecast_test(
    stmts: FinancialStatements,
    snapshot: SnapshotAssertion,
    request: FixtureRequest,
    adjusts: AdjustDict,
    exclude: Sequence[str] = tuple(),
    **fcst_kwargs,
):
    adjust_forecast_methods(stmts, adjusts)
    fcst = stmts.forecast(**{**FORECAST_KWARGS, **fcst_kwargs})
    if "--snapshot-update" in sys.argv:
        # Also save plots just like they are snapshots, though they are not being compared.
        # This is because it is easier to look at the plot visually but harder to do a diff
        fig = fcst.plot()
        out_path = pdf_path / f"{request.node.name}.pdf"
        fig.savefig(out_path)
    assert format_statement_for_snapshot(fcst, exclude=exclude) == snapshot
