from dataclasses import dataclass, field
from typing import Union, Dict


@dataclass
class ForecastConfig:
    periods: int = 5
    freq: str = 'Y'

    @property
    def make_future_df_kwargs(self) -> Dict[str, Union[int, str]]:
        return dict(
            periods=self.periods,
            freq=self.freq
        )


@dataclass
class ForecastItemConfig:
    method: str = 'auto'
    prophet_kwargs: dict = field(default_factory=lambda: {})
