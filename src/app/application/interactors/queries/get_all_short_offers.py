from dataclasses import dataclass
from typing import List, TypedDict

from app.application.common.ports.gateways.queries.offer import OfferQueryGateway
from app.application.interactors.base import InteractorStrict
from app.domain.offer.entity import Offer

@dataclass(frozen=True, slots=True)
class GetAllOffersShortRequest:
    pass


class GetAllOffersShortResponse(TypedDict):
    offers: List[Offer]


class GetAllOffersShortInteractor(InteractorStrict[GetAllOffersShortRequest, GetAllOffersShortResponse]):
    def __init__(self, offer_query_gateway: OfferQueryGateway):
        self._offer_query_gateway = offer_query_gateway

    async def __call__(self, request_data: GetAllOffersShortRequest) -> GetAllOffersShortResponse:
        offers = await self._offer_query_gateway.read_all()
        return GetAllOffersShortResponse(offers=offers)
