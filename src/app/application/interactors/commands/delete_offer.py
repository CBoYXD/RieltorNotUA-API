from dataclasses import dataclass
from typing import TypedDict

from app.application.common.ports.gateways.command.offer import OfferCommandGateway
from app.application.common.services.auth import AuthService
from app.application.common.ports.transaction_manager import TransactionManager
from app.application.interactors.base import InteractorStrict
from app.domain.base.value_object import Id
from app.domain.base.ports.uuid_generator import UUIDGenerator
from app.domain.offer.entity import Offer
from app.domain.offer.enums import OfferType, OfferPlaceType


@dataclass(frozen=True, slots=True)
class DeleteOfferRequest:
    offer_id: str

class DeleteOfferResponse(TypedDict):
    success: bool

class DeleteOfferInteractor(InteractorStrict[DeleteOfferRequest, DeleteOfferResponse]):
    def __init__(
        self,
        offer_command_gateway: OfferCommandGateway,
        auth_service: AuthService,
        transaction_manager: TransactionManager
    ):
        self._offer_command_gateway = offer_command_gateway
        self._auth_service = auth_service
        self._transaction_manager = transaction_manager

    async def __call__(self, request_data: DeleteOfferRequest) -> DeleteOfferResponse:
        await self._auth_service.authorize_action()
        
        await self._offer_command_gateway.delete(Id(request_data.offer_id))
        await self._transaction_manager.commit()
        
        return DeleteOfferResponse(success=True)