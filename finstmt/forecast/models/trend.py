from typing import Optional

import pandas as pd
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
from pandas import DatetimeIndex
from statsmodels.regression.linear_model import RegressionResults

from finstmt.forecast.models.base import ForecastModel
from finstmt.forecast.plot import plot_forecast


class LinearTrendModel(ForecastModel):
    model: Optional[sm.OLS] = None
    model_result: Optional[RegressionResults] = None
    orig_dates: Optional[DatetimeIndex] = None
    result_df: Optional[pd.DataFrame] = None

    def fit(self, series: pd.Series):
        X = sm.add_constant(np.arange(len(series)))
        self.model = sm.OLS(series, X)
        self.model_result = self.model.fit()
        self.orig_dates = series.index
        super().fit(series)

    def predict(self) -> pd.Series:
        last_t = len(self.model.exog) - 1
        future_X = sm.add_constant(np.arange(last_t + 1, last_t + self.config.periods + 1))
        future_dates = self._future_date_range
        all_X = np.concatenate((self.model.exog, future_X))
        all_dates = np.concatenate((self.orig_dates, future_dates))
        predicted = self.model_result.get_prediction(all_X)
        predict_df = predicted.summary_frame().set_index(all_dates)
        self.result_df = predict_df[['mean', 'mean_ci_lower', 'mean_ci_upper']].rename(
            columns={'mean_ci_lower': 'lower', 'mean_ci_upper': 'upper'}
        )
        self.result = self.result_df['mean'].loc[future_dates]
        super().predict()
        return self.result

    def plot(self) -> plt.Figure:
        return plot_forecast(self.result_df, self.model.endog, self.orig_dates)
