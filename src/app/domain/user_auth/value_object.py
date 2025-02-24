from dataclasses import dataclass
from datetime import datetime

from app.domain.base.value_object import ValueObject
from app.domain.user_auth.exceptions import TimestampError
from app.domain.user_auth.validation.functions import validation_password_length


@dataclass(frozen=True, repr=False)
class RawPassword(ValueObject):
    value: str

    def __post_init__(self):
        validation_password_length(self.value)


@dataclass(frozen=True, repr=False)
class UserPasswordHash(ValueObject):
    # TODO: Add validation
    value: str


@dataclass(frozen=True, repr=False)
class UserCreatedAt(ValueObject):
    """
    Ensures the 'created_at' timestamp is valid.

    :raises TimestampError: If the timestamp is invalid.
    """
    value: datetime


    def __post_init__(self):
        if self.value > datetime.now():
            raise TimestampError("CreatedAt",self.value)


    def __repr__(self) -> str:
        return f"CreatedAt({self.value.isoformat()})"


@dataclass(frozen=True, repr=False)
class UserUpdateAt(ValueObject):
    """
    Ensures the 'updated_at' timestamp is valid.

    :raises TimestampError: If the timestamp is invalid.
    """
    value: datetime | None

    def __post_init__(self):
        if self.value > datetime.now():
            raise TimestampError("UpdatedAt",self.value)


    def __repr__(self) -> str:
        return f"UpdatedAt({self.value.isoformat()})"