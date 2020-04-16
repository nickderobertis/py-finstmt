from dataclasses import dataclass, field
from typing import Union, Dict, Optional, Any, List

import pandas as pd


@dataclass
class ForecastConfig:
    periods: int = 5
    freq: str = 'Y'
    prophet_kwargs:  dict = field(default_factory=lambda: {})

    @property
    def make_future_df_kwargs(self) -> Dict[str, Union[int, str]]:
        return dict(
            periods=self.periods,
            freq=self.freq
        )


@dataclass
class ForecastItemConfig:
    """
    The main configuration for a single item forecast

    method: 'auto' currently only supported method, runs forecast with fbprophet
    pct_of: key of financial statement item to forecast this as a percentage of
    make_forecast: whether to forecast
    prophet_kwargs: kwargs to pass to fbprophet model
    cap: the maximum that the trend line should reach
    floot: the minimum that the trend line should reach
    """
    method: str = 'cagr'
    pct_of: Optional[str] = None
    make_forecast: bool = True
    prophet_kwargs: dict = field(default_factory=lambda: {})
    cap: Optional[Union[float, pd.Series]] = None
    floor: Optional[Union[float, pd.Series]] = None
    manual_forecasts: Dict[str, List[float]] = field(default_factory=lambda: {'levels': [], 'growth': []})

    def to_series(self) -> pd.Series:
        out_dict = {
            'Method': self.method,
            '% of': self.pct_of,
            'Cap': self.cap,
            'Floor': self.floor
        }
        out_dict.update(self.prophet_kwargs)
        if self.manual_forecasts['levels']:
            out_dict.update({'Manual Levels': self.manual_forecasts['levels']})
        if self.manual_forecasts['growth']:
            growth_pcts = [f'{growth:.2%}' for growth in self.manual_forecasts['growth']]
            out_dict.update({'Manual Growth': growth_pcts})
        return pd.Series(out_dict)

