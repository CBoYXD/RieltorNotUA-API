from dataclasses import dataclass

from app.domain.base.value_object import ValueObject


@dataclass(frozen=True, repr=False)
class RieltorAgencyName(ValueObject):
    value: str


@dataclass(frozen=True, repr=False)
class RieltorLicenseNumber(ValueObject):
    value: int


@dataclass(frozen=True, repr=False)
class RieltorExperienceYears(ValueObject):
    value: int
