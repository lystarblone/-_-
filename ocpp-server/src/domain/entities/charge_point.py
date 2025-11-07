from dataclasses import dataclass
from src.domain.enums import CpStatus
from src.domain.entities.session import Session
from datetime import datetime

@dataclass
class ChargePoint:
    id: str
    vendor: str
    model: str
    last_seen: datetime
    status: CpStatus
    sessions: list[Session]