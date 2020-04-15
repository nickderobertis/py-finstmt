from typing import Optional

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from finstmt.forecast.models.base import ForecastModel
from finstmt.forecast.plot import plot_forecast


class AverageModel(ForecastModel):
    mean: Optional[float] = None
    stderr: Optional[float] = None
    orig_series: Optional[pd.Series] = None

    def fit(self, series: pd.Series):
        self.mean = series.mean()
        self.stderr = series.std() / (len(series) ** 0.5)
        self.orig_series = series
        super().fit(series)

    def predict(self) -> pd.Series:
        all_dates = np.concatenate((self.orig_series.index, self._future_date_range))
        df = pd.DataFrame(index=all_dates)
        df['mean'] = self.mean
        df['lower'] = self.mean - 2 * self.stderr
        df['upper'] = self.mean + 2 * self.stderr
        self.result_df = df
        self.result = df['mean']
        super().predict()
        return self.result

    def plot(self) -> plt.Figure:
        return plot_forecast(self.result_df, self.orig_series.values, self.orig_series.index)
