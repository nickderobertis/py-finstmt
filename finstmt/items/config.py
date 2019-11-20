from dataclasses import dataclass
from typing import Sequence, Optional

from finstmt.forecast.config import ForecastItemConfig


@dataclass
class ItemConfig:
    key: str
    display_name: str

    extract_names: Optional[Sequence[str]] = None
    force_positive: bool = True
    forecast_config: ForecastItemConfig = ForecastItemConfig()
    expr_str: Optional[str] = None

    @property
    def primary_name(self) -> str:
        if self.extract_names is None:
            return self.key

        return self.extract_names[0]
