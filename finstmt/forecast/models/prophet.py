import logging
from typing import Optional

import pandas as pd

from finstmt.exc import ForecastNotFitException
from finstmt.forecast.config import ForecastItemConfig, ForecastConfig
from finstmt.forecast.models.base import ForecastModel
from finstmt.forecast.dataframe import add_cap_and_floor_to_df


class FBProphetModel(ForecastModel):
    result_df: Optional[pd.DataFrame] = None

    def __init__(self, config: ForecastConfig, item_config: ForecastItemConfig):
        super().__init__(config, item_config)
        Prophet = _try_import_fbprophet()

        all_kwargs = {}
        if config.freq.lower() == 'y':
            all_kwargs['yearly_seasonality'] = False
        all_kwargs.update(item_config.prophet_kwargs)
        all_kwargs.update(config.prophet_kwargs)
        model = Prophet(**all_kwargs)
        self.model = model

    def fit(self, series: pd.Series):
        self.model.fit(self._df_for_fit(series))
        super().fit(series)

    def predict(self) -> pd.Series:
        future = self.model.make_future_dataframe(**self.config.make_future_df_kwargs)
        add_cap_and_floor_to_df(future, self.item_config.cap, self.item_config.floor)
        forecast = self.model.predict(future)
        self.result_df = forecast
        result = forecast[['ds', 'yhat']].set_index('ds')['yhat']
        result = result[result.index > self.last_historical_period]
        self.result = result
        super().predict()
        return result

    def plot(self):
        return self.model.plot(self.result_df)

    def _df_for_fit(self, series: pd.Series) -> pd.DataFrame:
        df = pd.DataFrame(series).reset_index()
        df.columns = ['ds', 'y']
        add_cap_and_floor_to_df(df, self.item_config.cap, self.item_config.floor)

        return df


def _try_import_fbprophet():
    try:
        from fbprophet import Prophet

    except ImportError:
        raise ImportError('need to install fbprophet to use forecasting functionality with method auto. '
                          'see https://facebook.github.io/prophet/docs/installation.html')

    # Suppress excessive logging from fbprophet
    fbprophet_logger = logging.getLogger('fbprophet')
    fbprophet_logger.setLevel(logging.WARN)

    return Prophet