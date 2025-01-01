from dataclasses import dataclass

from app.domain.base.value_object import ValueObject


@dataclass(frozen=True, repr=False)
class LocationRegion(ValueObject):
    value: str


@dataclass(frozen=True, repr=False)
class LocationDistrict(ValueObject):
    value: str


@dataclass(frozen=True, repr=False)
class LocationMainLocality(ValueObject):
    value: str


@dataclass(frozen=True, repr=False)
class LocationStreet(ValueObject):
    value: str


@dataclass(frozen=True, repr=False)
class LocationHouseNumber(ValueObject):
    value: str


@dataclass(frozen=True, repr=False)
class LocationLatitude(ValueObject):
    value: str


@dataclass(frozen=True, repr=False)
class LocationLongitude(ValueObject):
    value: str


@dataclass(frozen=True, repr=False)
class LocationFormattedAdress(ValueObject):
    value: str
