from finstmt.forecast.config import ForecastItemConfig, ForecastConfig
from finstmt.forecast.models.base import ForecastModel
from finstmt.forecast.models.prophet import get_auto_model


def get_model(config: ForecastConfig, item_config: ForecastItemConfig) -> ForecastModel:
    if item_config.method == 'auto':
        return get_auto_model(config, item_config)

    # TODO [#11]: add other approaches to forecasting
    #
    # Methods to add:
    # - average
    # - trend (reg)
    # - trend (CAGR)
    raise NotImplementedError(f'need to implement method {item_config.method}')