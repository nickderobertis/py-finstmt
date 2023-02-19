from copy import deepcopy
from dataclasses import dataclass
from typing import Dict, Optional, Sequence, Tuple, Union

import matplotlib.pyplot as plt
import pandas as pd

from finstmt.exc import ForecastNotFitException, ForecastNotPredictedException
from finstmt.forecast.config import ForecastConfig, ForecastItemConfig
from finstmt.forecast.models.chooser import get_model
from finstmt.forecast.models.manual import ManualForecastModel
from finstmt.items.config import ItemConfig


@dataclass
class Forecast:
    """
    The main class to represent a forecast of an individual item.
    """

    orig_series: pd.Series
    config: ForecastConfig
    item_config: ForecastItemConfig
    base_config: ItemConfig
    pct_of_series: Optional[pd.Series] = None
    pct_of_config: Optional[ItemConfig] = None

    def __post_init__(self):
        self.model = get_model(self.config, self.item_config, self.base_config)

    def fit(self):
        self.model.fit(self.series)

    def predict(self) -> pd.Series:
        if not self.model.has_been_fit:
            raise ForecastNotFitException("call .fit before .predict")
        return self.model.predict()

    def plot(
        self, ax: Optional[plt.Axes] = None, figsize: Tuple[int, int] = (12, 5)
    ) -> plt.Figure:
        if not self.model.has_prediction:
            raise ForecastNotPredictedException("call .predict before .plot")
        return self.model.plot(ax=ax, figsize=figsize, title=self.name)

    def to_manual(
        self,
        use_levels: bool = False,
        adjustments: Optional[Union[Sequence[float], Dict[int, float]]] = None,
        replacements: Optional[Union[Sequence[float], Dict[int, float]]] = None,
    ):
        if not self.model.has_prediction:
            raise ForecastNotPredictedException(
                "call .fit then .predict before .to_manual"
            )

        if use_levels:
            values = self.result.values
            config_key = "levels"
            reset_key = "growth"
        else:
            # Growth
            values = self.result.pct_change().values
            # Fill in first growth
            values[0] = (self.result.iloc[0] - self.series.iloc[-1]) / self.series.iloc[
                -1
            ]
            config_key = "growth"
            reset_key = "levels"

        self.item_config.method = "manual"

        if adjustments is not None:
            if not isinstance(adjustments, dict) and len(adjustments) != len(values):
                raise ValueError(
                    f"must pass equal length adjustments as number of periods. "
                    f"Got {len(adjustments)} adjustments for {len(values)} periods"
                )
            adjustments = _adjust_to_dict(adjustments)
            for i, adj in adjustments.items():
                values[i] += adj

        if replacements is not None:
            if not isinstance(replacements, dict) and len(replacements) != len(values):
                raise ValueError(
                    f"must pass equal length adjustments as number of periods. "
                    f"Got {len(replacements)} adjustments for {len(values)} periods"
                )
            replacements = _replace_to_dict(replacements)
            for i, replace in replacements.items():
                values[i] = replace

        self.item_config.manual_forecasts[config_key] = list(values)
        self.item_config.manual_forecasts[reset_key] = []
        self.model = ManualForecastModel(
            self.config, self.item_config, self.base_config
        )
        self.model.fit(self.series)
        self.model.predict()

    @property
    def series(self) -> pd.Series:
        if self.pct_of_series is None:
            return self.orig_series
        else:
            return self.orig_series / self.pct_of_series

    @property
    def result(self) -> pd.Series:
        if not self.model.has_prediction:
            raise ForecastNotPredictedException(
                "call .fit then .predict before .result"
            )
        return self.model.result

    @property
    def name(self) -> str:
        if self.pct_of_config is None:
            return self.base_config.display_name

        # Percentage of series
        return f"{self.base_config.display_name} % {self.pct_of_config.display_name}"

    def copy(self) -> "Forecast":
        return deepcopy(self)

    def __round__(self, n: Optional[int] = None) -> "Forecast":
        new_fcst = self.copy()
        new_fcst.orig_series = round(new_fcst.orig_series, n)
        if new_fcst.pct_of_series is not None:
            new_fcst.pct_of_series = round(new_fcst.pct_of_series, n)
        if new_fcst.pct_of_config is not None:
            new_fcst.pct_of_config = round(new_fcst.pct_of_config, n)  # type: ignore[call-overload]
        new_fcst.item_config = round(new_fcst.item_config, n)  # type: ignore[call-overload]
        new_fcst.base_config = round(new_fcst.base_config, n)  # type: ignore[call-overload]
        return new_fcst


def _adjust_to_dict(
    seq_or_dict: Union[Sequence[float], Dict[int, float]]
) -> Dict[int, float]:
    if isinstance(seq_or_dict, dict):
        return seq_or_dict

    # If adjustment is 0 or None, skip the entry, otherwise add to the dict
    adjust_dict = {i: val for i, val in enumerate(seq_or_dict) if val}
    return adjust_dict


def _replace_to_dict(
    seq_or_dict: Union[Sequence[float], Dict[int, float]]
) -> Dict[int, float]:
    if isinstance(seq_or_dict, dict):
        return seq_or_dict

    replace_dict = {i: val for i, val in enumerate(seq_or_dict)}
    return replace_dict
