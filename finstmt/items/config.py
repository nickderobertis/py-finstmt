import dataclasses
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, Optional, Self, Sequence, TypeVar

from finstmt.forecast.config import ForecastItemConfig

T = TypeVar("T")


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

    def copy(self, **updates) -> Self:
        return dataclasses.replace(self, **updates)

    def __round__(self, n=None) -> "ItemConfig":
        return _apply_operation_to_item_config(self, n, round)


ItemConfigOperationData = ForecastItemConfig


def _apply_operation_to_item_config(
    item_config: ItemConfig,
    other: T,
    func: Callable[[ItemConfigOperationData, T], ItemConfigOperationData],
) -> ItemConfig:
    updates: Dict[str, Any] = {}
    updates["forecast_config"] = func(item_config.forecast_config, other)
    return item_config.copy(**updates)
