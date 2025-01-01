from abc import abstractmethod
from typing import Protocol, List

from src.app.domain.base.value_object import Id
from src.app.domain.offer.entity import Offer
from src.app.domain.offer_details.entity import OfferDetails


class CabinetRepository(Protocol):
    @abstractmethod
    async def get_all_offers(self, user_id: Id) -> list[Offer]:
        """
        :raises DataMapperError:
        """
        
    @abstractmethod
    async def get_all_full_offers(self, user_id: Id) -> list[OfferDetails]:
        """
        :raises DataMapperError:
        """

    @abstractmethod
    async def get_offer_by_id(self, user_id: Id, offer_id: Id) -> Offer | None:
        """
        :raises DataMapperError:
        """

    @abstractmethod
    async def get_full_offer_by_id(self, user_id: Id, offer_id: Id) -> OfferDetails | None:
        """
        :raises DataMapperError:
        """
        
    # TODO: Add changing settings
