import datetime
from typing import Optional, Tuple, Dict, Sequence

import pandas as pd
import matplotlib.pyplot as plt
from pandas import DatetimeIndex

from finstmt.exc import ForecastNotFitException, ForecastNotPredictedException
from finstmt.forecast.config import ForecastConfig, ForecastItemConfig
from finstmt.forecast.plot import plot_forecast
from finstmt.items.config import ItemConfig


class ForecastModel:
    result: Optional[pd.Series] = None
    result_df: Optional[pd.DataFrame] = None
    last_historical_period: Optional[datetime.datetime] = None
    orig_series: Optional[pd.Series] = None

    def __init__(self, config: ForecastConfig, item_config: ForecastItemConfig, base_config: ItemConfig):
        self.config = config
        self.item_config = item_config
        self.base_config = base_config
        self.has_been_fit = False
        self.has_prediction = False

    def fit(self, series: pd.Series):
        self.last_historical_period = series.index.max()
        self.has_been_fit = True
        self.orig_series = series

    def predict(self) -> pd.Series:
        self.has_prediction = True
        return pd.Series()

    def plot(self, ax: Optional[plt.Axes] = None, figsize: Tuple[int, int] = (12, 5),
             xlabel: Optional[str] = None, ylabel: Optional[str] = None) -> plt.Figure:
        if xlabel is None:
            xlabel = 'Time'
        if ylabel is None:
            ylabel = self.base_config.display_name

        if self.orig_series is None:
            raise ForecastNotPredictedException('call .fit then .predict before .plot')

        return plot_forecast(
            self.result_df,
            self.orig_series.values,
            self.orig_series.index,
            ax=ax,
            figsize=figsize,
            xlabel=xlabel,
            ylabel=ylabel
        )

    @property
    def _future_date_range(self) -> DatetimeIndex:
        if not self.has_been_fit:
            raise ForecastNotFitException('call .fit before ._future_date_range')
        return pd.date_range(
            start=self.last_historical_period,
            periods=self.config.periods + 1,
            freq=self.config.freq,
            closed='right'
        )
