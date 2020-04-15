from finstmt.forecast.config import ForecastItemConfig, ForecastConfig


def get_auto_model(config: ForecastConfig, item_config: ForecastItemConfig):
    Prophet = _try_import_fbprophet()

    all_kwargs = {}
    if config.freq.lower() == 'y':
        all_kwargs['yearly_seasonality'] = False
    all_kwargs.update(item_config.prophet_kwargs)
    all_kwargs.update(config.prophet_kwargs)
    model = Prophet(**all_kwargs)
    return model


def _try_import_fbprophet():
    try:
        from fbprophet import Prophet
        return Prophet
    except ImportError:
        raise ImportError('need to install fbprophet to use forecasting functionality with method auto. '
                          'see https://facebook.github.io/prophet/docs/installation.html')