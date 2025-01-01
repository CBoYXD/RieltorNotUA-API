from dataclasses import dataclass
from typing import Optional

from app.domain.base.entity import Entity
from app.domain.base.value_object import Id
from app.domain.base.ports.uuid_generator import UUIDGenerator
from app.domain.location.value_object import (
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

    def create(
        id_generator: UUIDGenerator,
        offer_id: Id,
        region: str,
        district: str,
        main_locality: str,
        latitude: str,
        longitude: str,
        formatted_address: str,
        street: str | None = None,
        house_number: str | None = None,
    ) -> Location:
        return Location(
            id_=Id(id_generator()),
            offer_id=offer_id,
            region=LocationRegion(region),
            district=LocationDistrict(district),
            main_locality=LocationMainLocality(main_locality),
            street=LocationStreet(street) if street else None,
            house_number=LocationHouseNumber(house_number) if house_number else None,
            latitude=LocationLatitude(latitude),
            longitude=LocationLongitude(longitude),
            formatted_adress=LocationFormattedAdress(formatted_address)
        )
