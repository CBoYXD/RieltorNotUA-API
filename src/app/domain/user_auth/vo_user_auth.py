from dataclasses import dataclass
from pydantic import EmailStr
from uuid import UUID

from app.domain.base.value_object import ValueObject


@dataclass(frozen=True, repr=False)
class UserPasswordHash(ValueObject):
    # TODO: Add validation
    value: str
