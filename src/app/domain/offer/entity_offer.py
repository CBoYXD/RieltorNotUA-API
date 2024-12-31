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

    def create(
        id_generator: UUIDGenerator,
        author_id: Id,
        place_type: OfferPlaceType,
        offer_type: OfferType,
        area: float,
        name: str,
        price: int
    ) -> Offer:
        return Offer(
            id_=Id(id_generator()),
            author_id=author_id,
            place_type=place_type,
            offer_type=offer_type,
            area=OfferArea(area),
            name=OfferName(name),
            price=OfferPrice(price)
        )
