from abc import abstractmethod
from datetime import datetime
from typing import Protocol

class TimestampManager(Protocol):
    @abstractmethod
    def current_time(self) -> datetime:
        """Return the current time in the desired format"""
        ...


    @abstractmethod
    def update_time(self, time_filed: datetime) -> datetime:
        """Return the updated time_filed in the desired format"""
        ...

