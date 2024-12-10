from dataclasses import dataclass

from app.domain.base.value_object import ValueObject


@dataclass(frozen=True, repr=False)
class TagKey(ValueObject):
    value: str


@dataclass(frozen=True, repr=False)
class TagValue(ValueObject):
    value: str
