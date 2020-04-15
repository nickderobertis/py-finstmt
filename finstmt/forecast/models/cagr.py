from typing import Optional

import pandas as pd
import matplotlib.pyplot as plt

from finstmt.forecast.models.base import ForecastModel
from finstmt.forecast.plot import plot_forecast


class CAGRModel(ForecastModel):
    cagr: Optional[float] = None
    stderr: Optional[float] = None
    last_value: Optional[float] = None
    orig_series: Optional[pd.Series] = None

    def fit(self, series: pd.Series):
        y_T = series.iloc[-1]
        y_0 = series.iloc[0]
        n = len(series)
        self.cagr = (y_T / y_0) ** (1 / n) - 1
        self.stderr = series.pct_change().std() / (n ** 0.5)
        self.last_value = y_T
        self.orig_series = series
        super().fit(series)

    def predict(self) -> pd.Series:
        cagr_dict = dict(
            lower=self.cagr - self.stderr * 2,
            upper=self.cagr + self.stderr * 2,
            mean=self.cagr
        )

        # Start from last period, apply growth to predict into future
        future_df = pd.DataFrame(index=self._future_date_range)
        for col_name, cagr in cagr_dict.items():
            last_value = self.last_value
            future_values = []
            for _ in range(self.config.periods):
                next_value = last_value * (1 + cagr)
                future_values.append(next_value)
                last_value = next_value
            future_df[col_name] = future_values
        self.result = future_df['mean']

        # Start from last period, work back to earliest period removing growth to assess fit
        orig_dates = self.orig_series.index
        past_df = pd.DataFrame(index=reversed(orig_dates))
        for col_name, cagr in cagr_dict.items():
            last_value = self.last_value
            past_values = [self.last_value]
            for _ in range(len(orig_dates) - 1):
                next_value = last_value / (1 + cagr)
                past_values.append(next_value)
                last_value = next_value
            past_df[col_name] = past_values

        self.result_df = past_df.append(future_df).sort_index()
        super().predict()
        return self.result

    def plot(self) -> plt.Figure:
        return plot_forecast(self.result_df, self.orig_series.values, self.orig_series.index)
