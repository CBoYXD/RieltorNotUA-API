from dataclasses import dataclass, asdict

from app.domain.base.value_object import Id
from app.domain.offer.entity_offer import Offer
from app.domain.offer_details.vo_offer_details import OfferDetailsDescription
from app.domain.base.id_generator import UUIDGenerator


@dataclass(eq=False, kw_only=True)
class OfferDetails(Offer):
    description: OfferDetailsDescription
    tags: list[Id]
    photos: list[Id]

    def create(
        id_generator: UUIDGenerator,
        offer: Offer,
        description: str,
        tags: list[Id],
        photos: list[Id]
    ) -> OfferDetails:
        return OfferDetails(
            description=OfferDetailsDescription(description),
            tags=tags,
            photos=photos,
            **asdict(offer)
        )
