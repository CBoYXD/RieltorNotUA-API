from dataclasses import dataclass, asdict

from app.domain.base.value_object import Id
from app.domain.offer.entity import Offer
from app.domain.offer_details.value_object import (
    OfferDetailsDescription, 
    OfferDetailsPhoto, 
    OfferDetailsTag
)
from app.domain.base.ports.uuid_generator import UUIDGenerator


@dataclass(eq=False, kw_only=True)
class OfferDetails(Offer):
    description: OfferDetailsDescription
    tags: list[Id]
    photos: list[OfferDetailsPhoto]

    def create(
        id_generator: UUIDGenerator,
        offer: Offer,
        description: str,
        tags: list[str],
        photos: list[str]
    ) -> OfferDetails:
        return OfferDetails(
            description=OfferDetailsDescription(description),
            tags=[OfferDetailsTag(tag) for tag in tags],
            photos=[OfferDetailsPhoto(photo) for photo in photos],
            **asdict(offer)
        )
