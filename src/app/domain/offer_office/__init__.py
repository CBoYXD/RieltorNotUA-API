from dataclasses import dataclass
from app.domain.offer.entity_offer import Offer


@dataclass(eq=False, kw_only=True)
class OfferOffice(Offer):
    floors: list[int]
    # Add more fields
