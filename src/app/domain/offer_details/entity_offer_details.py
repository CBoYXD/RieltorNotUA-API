from dataclasses import dataclass

from app.domain.base.value_object import Id
from app.domain.offer.entity_offer import Offer
from app.domain.offer_details.vo_offer_details import OfferDetailsDescription


@dataclass(eq=False, kw_only=True)
class OfferDetails(Offer):
    description: OfferDetailsDescription
    tags: list[Id]
    photos: list[Id]
