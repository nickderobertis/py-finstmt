from dataclasses import dataclass, field
from typing import Optional, Sequence

from finstmt.forecast.config import ForecastItemConfig


@dataclass
class ItemConfig:
    key: str
    display_name: str

    extract_names: Optional[Sequence[str]] = None
    force_positive: bool = True
    forecast_config: ForecastItemConfig = field(
        default_factory=lambda: ForecastItemConfig()
    )
    expr_str: Optional[str] = None

    # TODO [#19]: add config and logic for whether to take highest priority or add all of matching names
    #
    # When extracting impairment, in Capital IQ data it has Impairment of Goodwill and Asset Writedown,
    # both of which should be included. This is in contrast to most others where only the highest priority
    # key should be selected

    @property
    def primary_name(self) -> str:
        if self.extract_names is None:
            return self.key

        return self.extract_names[0]

    class Config:
        arbitrary_types_allowed = True
