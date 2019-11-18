from dataclasses import dataclass, field
from typing import Union, Dict, Optional, Any

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
    method: str = 'auto'
    pct_of: Optional[str] = None
    make_forecast: bool = True
    prophet_kwargs: dict = field(default_factory=lambda: {})

    def to_series(self) -> pd.Series:
        out_dict = {
            'Method': self.method,
            '% of': self.pct_of
        }
        out_dict.update(self.prophet_kwargs)
        return pd.Series(out_dict)

