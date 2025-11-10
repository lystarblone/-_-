from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Session:
    id: str
    cp_id: str
    start_time: datetime
    end_time: Optional[datetime]
    meter_start: float
    meter_stop: Optional[float]
    energy_consumed: float
    active: bool = True