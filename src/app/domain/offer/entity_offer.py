from dataclasses import dataclass
from typing import Optional
from uuid import UUID

from app.domain.offer.enums import OfferType
from app.domain.base.entity import Entity
from app.domain.base.value_object import Id
from app.domain.offer.vo_offer import (
    OfferArea,
    OfferName,
    OfferDescription,
    OfferLocation,
    OfferPrice,
    OfferFloor,
    OfferPhoto,
    OfferTag
)



@dataclass(eq=False, kw_only=True)
class Offer(Entity[Id]):
    author_id: Id
    offer_type: OfferType
    area: OfferArea
    name: OfferName
    description: OfferDescription
    location: OfferLocation
    geocoding_location: dict
    price: OfferPrice
    floor: OfferFloor
    photos: list[OfferPhoto]
    tags: Optional[list[OfferTag]]
