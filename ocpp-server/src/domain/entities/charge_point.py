from dataclasses import dataclass
from src.domain.enums import CpStatus
from datetime import datetime
from typing import List

@dataclass
class ChargePoint:
    id: str
    vendor: str
    model: str
    last_seen: datetime
    status: CpStatus
    sessions: List[str]