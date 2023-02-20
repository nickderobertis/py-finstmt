"""
Forecast snapshot tests

Note that the outputted numbers in the snapshot are divided by 1000 and rounded
to make the snapshot consistent across different machines.

When updating snapshots, check the generated folder for PDFs of the plots.
"""
import sys
from typing import Final, Sequence

import matplotlib
import pytest
from _pytest.fixtures import FixtureRequest
from syrupy import SnapshotAssertion

from finstmt import FinancialStatements
from finstmt.exc import BalanceSheetNotBalancedException
from tests.config import GENERATED_PATH
from tests.fixtures.forecast.adjust_config import (
    FORECAST_ADJUSTS,
    AdjustDict,
    adjust_forecast_methods,
)
from tests.snapshot.forecast.snapshot_format import format_statement_for_snapshot

matplotlib.use("Agg")

FORECAST_KWARGS: Final = dict(periods=2)

pdf_path = GENERATED_PATH / "test_forecast_pdfs"
pdf_path.mkdir(parents=True, exist_ok=True)


def test_forecast_annual_stockrow_cat(
    annual_stockrow_stmts_cat: FinancialStatements, snapshot, request
):
    stmts = annual_stockrow_stmts_cat

    _forecast_test(
        stmts,
        snapshot,
        request,
        FORECAST_ADJUSTS["stockrow_cat"],
        exclude=("gross_ppe", "dep"),
    )


def test_forecast_annual_stockrow_cat_no_balance(
    annual_stockrow_stmts_cat: FinancialStatements, snapshot, request
):
    stmts = annual_stockrow_stmts_cat

    _forecast_test(
        stmts,
        snapshot,
        request,
        FORECAST_ADJUSTS["stockrow_cat"],
        exclude=("gross_ppe", "dep"),
        balance=False,
    )


def test_forecast_annual_stockrow_cat_change_bs_diff(
    annual_stockrow_stmts_cat: FinancialStatements, snapshot, request
):
    stmts = annual_stockrow_stmts_cat

    _forecast_test(
        stmts,
        snapshot,
        request,
        FORECAST_ADJUSTS["stockrow_cat"],
        exclude=("gross_ppe", "dep"),
        bs_diff_max=100000,
    )


def test_forecast_annual_stockrow_cat_make_forecast_and_plug(
    annual_stockrow_stmts_cat: FinancialStatements, snapshot, request
):
    stmts = annual_stockrow_stmts_cat.copy()
    stmts.config.update("total_debt", ["forecast_config", "make_forecast"], True)
    stmts.config.update("st_debt", ["forecast_config", "make_forecast"], False)
    stmts.config.update("def_tax_lt", ["forecast_config", "method"], "manual")
    stmts.config.update(
        "def_tax_lt",
        ["forecast_config", "manual_forecasts"],
        {"levels": [], "growth": [4, 5]},
    )

    with pytest.raises(BalanceSheetNotBalancedException):
        _forecast_test(
            stmts,
            snapshot,
            request,
            FORECAST_ADJUSTS["stockrow_cat"],
            exclude=("gross_ppe", "dep"),
        )

    stmts.config.update("total_debt", ["forecast_config", "plug"], True)
    stmts.config.update("lt_debt", ["forecast_config", "plug"], False)

    _forecast_test(
        stmts,
        snapshot,
        request,
        FORECAST_ADJUSTS["stockrow_cat"],
        exclude=("gross_ppe", "dep"),
    )


def test_forecast_quarterly_stockrow_cat(
    quarterly_stockrow_stmts_cat: FinancialStatements, snapshot, request
):
    stmts = quarterly_stockrow_stmts_cat

    _forecast_test(
        stmts,
        snapshot,
        request,
        FORECAST_ADJUSTS["stockrow_cat"],
        exclude=("gross_ppe", "dep"),
    )


def test_forecast_annual_stockrow_mar(
    annual_stockrow_stmts_mar: FinancialStatements, snapshot, request
):
    stmts = annual_stockrow_stmts_mar
    stmts.config.update("cash", ["forecast_config", "plug"], False)
    stmts.config.update("cash_and_st_invest", ["forecast_config", "plug"], True)

    _forecast_test(
        stmts,
        snapshot,
        request,
        FORECAST_ADJUSTS["stockrow_mar"],
        exclude=("gross_ppe", "dep"),
    )


def test_forecast_quarterly_stockrow_mar(
    quarterly_stockrow_stmts_mar: FinancialStatements, snapshot, request
):
    stmts = quarterly_stockrow_stmts_mar
    stmts.config.update("cash", ["forecast_config", "plug"], False)
    stmts.config.update("cash_and_st_invest", ["forecast_config", "plug"], True)

    _forecast_test(
        stmts,
        snapshot,
        request,
        FORECAST_ADJUSTS["stockrow_mar"],
        exclude=("gross_ppe", "dep"),
    )


def test_forecast_annual_capiq_cat(
    annual_capiq_stmts: FinancialStatements, snapshot, request
):
    stmts = annual_capiq_stmts

    _forecast_test(
        stmts,
        snapshot,
        request,
        FORECAST_ADJUSTS["capiq"],
    )


def test_forecast_quarterly_capiq_cat(
    quarterly_capiq_stmts: FinancialStatements, snapshot, request
):
    stmts = quarterly_capiq_stmts

    _forecast_test(
        stmts,
        snapshot,
        request,
        FORECAST_ADJUSTS["capiq"],
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
