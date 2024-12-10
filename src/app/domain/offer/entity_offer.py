from dataclasses import dataclass

from app.domain.base.entity import Entity
from app.domain.base.value_object import Id
from app.domain.offer.enums import OfferPlaceType, OfferType
from app.domain.offer.vo_offer import OfferArea, OfferName, OfferPrice


@dataclass(eq=False, kw_only=True)
class Offer(Entity[Id]):
    author_id: Id
    place_type: OfferPlaceType
    offer_type: OfferType
    area: OfferArea
    name: OfferName
    price: OfferPrice
