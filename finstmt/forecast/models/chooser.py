from finstmt.forecast.config import ForecastItemConfig, ForecastConfig
from finstmt.forecast.models.base import ForecastModel
from finstmt.forecast.models.prophet import FBProphetModel
from finstmt.forecast.models.trend import LinearTrendModel


def get_model(config: ForecastConfig, item_config: ForecastItemConfig) -> ForecastModel:
    if item_config.method == 'auto':
        return FBProphetModel(config, item_config)
    elif item_config.method == 'trend':
        return LinearTrendModel(config, item_config)

    # TODO [#11]: add other approaches to forecasting
    #
    # Methods to add:
    # - average
    # - trend (CAGR)
    raise NotImplementedError(f'need to implement method {item_config.method}')