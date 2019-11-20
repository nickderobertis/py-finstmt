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
