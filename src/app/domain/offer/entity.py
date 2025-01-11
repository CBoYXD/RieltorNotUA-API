from dataclasses import dataclass

from app.domain.base.entity import Entity
from app.domain.base.value_object import Id
from app.domain.base.ports.uuid_generator import UUIDGenerator
from app.domain.offer.enums import OfferPlaceType, OfferType
from app.domain.offer.value_object import OfferArea, OfferName, OfferPrice


@dataclass(eq=False, kw_only=True)
class Offer(Entity[Id]):
    # RO model
    author_id: Id
    place_type: OfferPlaceType
    offer_type: OfferType
    area: OfferArea
    name: OfferName
    price: OfferPrice
    formatted_address: str

    def create(
        id_generator: UUIDGenerator,
        author_id: Id,
        place_type: OfferPlaceType,
        offer_type: OfferType,
        area: float,
        name: str,
        price: int,
        formatted_address: str
    ) -> Offer:
        return Offer(
            id_=Id(id_generator()),
            author_id=author_id,
            place_type=place_type,
            offer_type=offer_type,
            area=OfferArea(area),
            name=OfferName(name),
            price=OfferPrice(price),
            formatted_address=str
        )
