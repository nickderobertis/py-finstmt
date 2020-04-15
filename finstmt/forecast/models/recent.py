from typing import Optional

import pandas as pd
import numpy as np

from finstmt.forecast.models.base import ForecastModel


class RecentValueModel(ForecastModel):
    recent: Optional[float] = None

    def fit(self, series: pd.Series):
        self.recent = series.iloc[-1]
        super().fit(series)

    def predict(self) -> pd.Series:
        all_dates = np.concatenate((self.orig_series.index, self._future_date_range))
        df = pd.DataFrame(index=all_dates)
        df['mean'] = self.recent
        self.result_df = df
        self.result = df['mean']
        super().predict()
        return self.result
