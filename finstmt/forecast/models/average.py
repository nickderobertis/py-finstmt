from typing import Optional

import pandas as pd
import numpy as np

from finstmt.forecast.models.base import ForecastModel


class AverageModel(ForecastModel):
    mean: Optional[float] = None
    stderr: Optional[float] = None

    def fit(self, series: pd.Series):
        self.mean = series.mean()
        self.stderr = series.std() / (len(series) ** 0.5)
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
