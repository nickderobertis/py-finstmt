from dataclasses import dataclass, field
from typing import Dict, List, Optional, Union

import pandas as pd


@dataclass
class ForecastConfig:
    periods: int = 5
    freq: str = "Y"
    prophet_kwargs: dict = field(default_factory=lambda: {})
    balance: bool = True
    timeout: float = 180

    # TODO [#45]: after handling units, adjust default allowed BS difference for units
    bs_diff_max: float = 10000

    def __post_init__(self):
        if self.freq.casefold() == "y":
            self.freq = "12m"
        elif self.freq.casefold() == "q":
            self.freq = "3m"

    @property
    def make_future_df_kwargs(self) -> Dict[str, Union[int, str]]:
        return dict(periods=self.periods, freq=self.freq)


@dataclass
class ForecastItemConfig:
    """
    The main configuration for a single item forecast

    method: 'auto' currently only supported method, runs forecast with prophet
    pct_of: key of financial statement item to forecast this as a percentage of
    make_forecast: whether to forecast
    prophet_kwargs: kwargs to pass to prophet model
    cap: the maximum that the trend line should reach
    floor: the minimum that the trend line should reach
    manual_forecasts: manually set values to use instead of doing a forecast
    plug: Whether to make this item adjustable to balance the balance sheet
    balance_item: Whether this item is balanced in the balancing process after forecasting
        and which item to balance it with (typically just set to 'total_liab_and_equity' for
        total assets and 'total_assets' for total liabilities and equity)
    """

    method: str = "cagr"
    pct_of: Optional[str] = None
    make_forecast: bool = True
    prophet_kwargs: dict = field(default_factory=lambda: {})
    cap: Optional[Union[float, pd.Series]] = None
    floor: Optional[Union[float, pd.Series]] = None
    manual_forecasts: Dict[str, List[float]] = field(
        default_factory=lambda: {"levels": [], "growth": []}
    )
    plug: bool = False
    balance_with: Optional[str] = None

    def to_series(self) -> pd.Series:
        out_dict = {
            "Method": self.method,
            "% of": self.pct_of,
            "Cap": self.cap,
            "Floor": self.floor,
            "Plug": self.plug,
        }
        out_dict.update(self.prophet_kwargs)
        if self.manual_forecasts["levels"]:
            out_dict.update({"Manual Levels": self.manual_forecasts["levels"]})
        if self.manual_forecasts["growth"]:
            growth_pcts = [
                f"{growth:.2%}" for growth in self.manual_forecasts["growth"]
            ]
            out_dict.update({"Manual Growth": growth_pcts})
        return pd.Series(out_dict)
