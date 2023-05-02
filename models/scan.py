from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class ScanStatus(Enum):
    ACCEPTED = 1
    RUNNING = 2
    ERROR = 3
    COMPLETE = 4
    NOT_FOUND = 5


@dataclass
class Scan:
    status: ScanStatus
    url: str
    scan_id: int | None = None
    finish_time: int | None = None
