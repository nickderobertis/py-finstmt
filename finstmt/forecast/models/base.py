import datetime
from typing import Optional

import pandas as pd
import matplotlib.pyplot as plt

from finstmt.forecast.config import ForecastConfig, ForecastItemConfig


class ForecastModel:
    result: Optional[pd.Series] = None
    last_historical_period: Optional[datetime.datetime] = None

    def __init__(self, config: ForecastConfig, item_config: ForecastItemConfig):
        self.config = config
        self.item_config = item_config
        self.has_been_fit = False
        self.has_prediction = False

    def fit(self, series: pd.Series):
        self.last_historical_period = series.index.max()
        self.has_been_fit = True

    def predict(self) -> pd.Series:
        self.has_prediction = True
        return pd.Series()

    def plot(self) -> plt.Axes:
        raise NotImplementedError