import math
import warnings
from dataclasses import dataclass, field
from typing import Dict, Sequence, Optional, Tuple

import matplotlib.pyplot as plt

from finstmt.combined.statements import FinancialStatements
from finstmt.forecast.main import Forecast

NUM_PLOT_COLUMNS = 3
DEFAULT_WIDTH = 15
DEFAULT_HEIGHT_PER_ROW = 3

@dataclass
class ForecastedFinancialStatements(FinancialStatements):
    forecasts: Dict[str, Forecast] = field(default_factory=lambda: {})

    def plot(self, subset: Optional[Sequence[str]] = None, figsize: Optional[Tuple[int, int]] = None) -> plt.Figure:
        if subset is not None:
            plot_items = {k: v for k, v in self.forecasts.items() if k in subset}
        else:
            plot_items = self.forecasts

        num_plot_rows = math.ceil(len(plot_items) / NUM_PLOT_COLUMNS)
        num_plot_columns = min(len(plot_items), NUM_PLOT_COLUMNS)

        if figsize is None:
            figsize = (DEFAULT_WIDTH, DEFAULT_HEIGHT_PER_ROW * num_plot_rows)

        fig, axes = plt.subplots(num_plot_rows, num_plot_columns, sharex='col', sharey=False, figsize=figsize)
        row = 0
        col = 0
        with warnings.catch_warnings():
            warnings.filterwarnings(action='ignore', message='Attempting to set identical bottom == top')
            for item_key, forecast in plot_items.items():
                if num_plot_rows == 1:
                    # 1D array if single row
                    forecast.plot(ax=axes[col])
                else:
                    # 2D array if multiple rows
                    forecast.plot(ax=axes[row, col])
                col += 1
                if col == num_plot_columns:
                    row += 1
                    col = 0
        return fig