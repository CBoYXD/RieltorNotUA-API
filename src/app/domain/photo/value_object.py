from dataclasses import dataclass

from app.domain.base.value_object import ValueObject


@dataclass(frozen=True, repr=False)
class PhotoExtenstion(ValueObject):
    value: str


@dataclass(frozen=True, repr=False)
class PhotoName(ValueObject):
    value: str
