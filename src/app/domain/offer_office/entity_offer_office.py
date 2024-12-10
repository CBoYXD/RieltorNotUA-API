from dataclasses import dataclass
from app.domain.offer.entity_offer import Offer
from app.domain.offer.vo_offer import OfferFloor


@dataclass(eq=False, kw_only=True)
class OfferOffice(Offer):
    floors: list[OfferFloor]
    # Add more fields
