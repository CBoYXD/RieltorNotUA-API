from dataclasses import dataclass
from typing import List, TypedDict

from app.application.common.ports.gateways.queries.offer import OfferQueryGateway
from app.application.interactors.base import InteractorStrict
from app.domain.offer_details.entity import OfferDetails


@dataclass(frozen=True, slots=True)
class GetAllOffersRequest:
    pass


class GetAllOffersResponse(TypedDict):
    offers: List[OfferDetails]


class GetAllOffersInteractor(InteractorStrict[GetAllOffersRequest, GetAllOffersResponse]):
    def __init__(self, offer_query_gateway: OfferQueryGateway):
        self._offer_query_gateway = offer_query_gateway

    async def __call__(self, request_data: GetAllOffersRequest) -> GetAllOffersResponse:
        offers = await self._offer_query_gateway.read_all_full_offers()
        return GetAllOffersResponse(offers=offers)
