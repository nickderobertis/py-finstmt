from copy import deepcopy
from typing import Optional

import pandas as pd

from finstmt.forecast.config import ForecastConfig, ForecastItemConfig


class Forecast:
    """
    The main class to represent a forecast of an individual item.
    """

    def __init__(self, series: pd.Series, config: ForecastConfig, item_config: ForecastItemConfig,
                 pct_of_series: Optional[pd.Series] = None):
        try:
            from fbprophet import Prophet
        except ImportError:
            raise ImportError('need to install fbprophet to use forecasting functionality. '
                              'see https://facebook.github.io/prophet/docs/installation.html')

        self.orig_series = series
        self.config = config
        self.item_config = item_config
        self.pct_of_series = pct_of_series

        if self.item_config.method == 'auto':
            all_kwargs = {}
            if self.config.freq.lower() == 'y':
                all_kwargs['yearly_seasonality'] = False
            all_kwargs.update(self.item_config.prophet_kwargs)
            all_kwargs.update(self.config.prophet_kwargs)
            self.model = Prophet(**all_kwargs)
        else:
            # TODO: add average approach
            raise NotImplementedError(f'need to implement method {self.item_config.method}')

        # Set in other methods
        self.result_df = None
        self.result = None

    def fit(self) -> pd.Series:
        self.model.fit(self._df_for_fit)
        future = self.model.make_future_dataframe(**self.config.make_future_df_kwargs)
        forecast = self.model.predict(future)
        self.result_df = forecast
        result = forecast[['ds', 'yhat']].set_index('ds')['yhat']
        result = result[result.index > self.orig_series.index.max()]
        self.result = result
        return result

    def plot(self):
        return self.model.plot(self.result_df)

    def plot_components(self):
        return self.model.plot_components(self.result_df)

    @property
    def _df_for_fit(self) -> pd.DataFrame:
        if self.pct_of_series is None:
            series = self.orig_series
        else:
            series = self.orig_series / self.pct_of_series

        df = pd.DataFrame(series).reset_index()
        df.columns = ['ds', 'y']
        return df



