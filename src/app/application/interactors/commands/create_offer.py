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
class CreateOfferRequest:
    place_type: OfferPlaceType
    offer_type: OfferType
    area: float
    name: str
    price: int
    formatted_address: str


class CreateOfferResponse(TypedDict):
    offer_id: str

class CreateOfferInteractor(InteractorStrict[CreateOfferRequest, CreateOfferResponse]):
    def __init__(
        self,
        offer_command_gateway: OfferCommandGateway,
        auth_service: AuthService,
        transaction_manager: TransactionManager,
        uuid_generator: UUIDGenerator
    ):
        self._offer_command_gateway = offer_command_gateway
        self._auth_service = auth_service
        self._transaction_manager = transaction_manager
        self._uuid_generator = uuid_generator

    async def __call__(self, request_data: CreateOfferRequest) -> CreateOfferResponse:
        # Check authorization
        await self._auth_service.authorize_action()

        offer = Offer.create(
            id_generator=self._uuid_generator,
            author_id=await self._auth_service.get_current_user_id(),
            place_type=request_data.place_type,
            offer_type=request_data.offer_type,
            area=request_data.area,
            name=request_data.name,
            price=request_data.price,
            formatted_address=request_data.formatted_address
        )

        await self._offer_command_gateway.save(offer)
        await self._transaction_manager.commit()

        return CreateOfferResponse(offer_id=str(offer.id_.value))
