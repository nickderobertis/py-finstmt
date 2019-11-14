from dataclasses import dataclass
from typing import Sequence, Optional


@dataclass
class ItemConfig:
    key: str
    display_name: str

    extract_names: Optional[Sequence[str]] = None
    force_positive: bool = True
