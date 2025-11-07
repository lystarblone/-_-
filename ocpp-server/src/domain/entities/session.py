from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from src.domain.entities.charge_point import ChargePoint

@dataclass
class Session:
    id: str
    cp_id: str | ChargePoint.id
    start_time: datetime
    end_time: Optional[datetime]
    meter_start: float
    meter_stop: Optional[float]
    energy_consumed: float
    active: bool = True