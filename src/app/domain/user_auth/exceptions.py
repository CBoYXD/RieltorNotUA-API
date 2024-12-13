from datetime import datetime
from pyexpat.errors import messages

from src.app.domain.base.exceptions import DomainFieldError


class TimestampError(DomainFieldError):
    def __init__(self, field_name: str, time: datetime):
        message: str = f"{field_name} '{time}' cannot be in the future."
        super().__init__(message)
