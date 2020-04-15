from copy import deepcopy
from typing import Optional

import pandas as pd
import matplotlib.pyplot as plt

from finstmt.exc import ForecastNotFitException, ForecastNotPredictedException
from finstmt.forecast.config import ForecastConfig, ForecastItemConfig
from finstmt.forecast.models.base import ForecastModel

from finstmt.forecast.models.chooser import get_model


class Forecast:
    """
    The main class to represent a forecast of an individual item.
    """
    model: ForecastModel

    def __init__(self, series: pd.Series, config: ForecastConfig, item_config: ForecastItemConfig,
                 pct_of_series: Optional[pd.Series] = None):
        self.orig_series = series
        self.config = config
        self.item_config = item_config
        self.pct_of_series = pct_of_series

        self.model = get_model(config, item_config)

    def fit(self):
        self.model.fit(self.series)

    def predict(self) -> pd.Series:
        if not self.model.has_been_fit:
            raise ForecastNotFitException('call .fit before .predict')
        return self.model.predict()

    def plot(self) -> plt.Axes:
        if not self.model.has_prediction:
            raise ForecastNotPredictedException('call .predict before .plot')
        return self.model.plot()

    @property
    def series(self) -> pd.Series:
        if self.pct_of_series is None:
            return self.orig_series
        else:
            return self.orig_series / self.pct_of_series

    @property
    def result(self) -> pd.Series:
        if not self.model.has_prediction:
            raise ForecastNotPredictedException('call .fit then .predict before .result')
        return self.model.result






