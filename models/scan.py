from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class ScanStatus(Enum):
    ACCEPTED = 1
    RUNNING = 2
    ERROR = 3
    COMPLETE = 4


@dataclass
class Scan:
    status: ScanStatus
    url: str
    scan_id: str | None = None
    finish_time: datetime | None = None
