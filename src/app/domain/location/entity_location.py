from dataclasses import dataclass
from typing import Optional

from app.domain.base.entity import Entity
from app.domain.base.value_object import Id
from app.domain.location.vo_location import (
    LocationDistrict,
    LocationFormattedAdress,
    LocationHouseNumber,
    LocationLatitude,
    LocationLongitude,
    LocationMainLocality,
    LocationRegion,
    LocationStreet,
)


@dataclass(eq=False, kw_only=True)
class Location(Entity[Id]):
    offer_id: Id
    region: LocationRegion
    district: LocationDistrict
    main_locality: LocationMainLocality  # City or village, etc.
    street: Optional[LocationStreet] = None
    house_number: Optional[LocationHouseNumber] = None
    latitude: LocationLatitude
    longitude: LocationLongitude
    formatted_adress: LocationFormattedAdress
