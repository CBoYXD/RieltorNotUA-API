from abc import abstractmethod
from typing import Protocol, List

from src.app.domain.base.value_object import Id
from src.app.domain.offer.entity import Offer
from src.app.domain.offer_details.entity import OfferDetails


class OfferRepository(Protocol):
    @abstractmethod
    async def search_offer(self, *args) -> list[Offer]:
        # TODO: Think how to represent search parameters
        """
        :raises DataMapperError:
        """
    
    @abstractmethod
    async def get_all_offers(self, limit: int = None) -> list[Offer]:
        """
        :raises DataMapperError:
        """
        
    @abstractmethod
    async def get_all_full_offers(self, limit: int = None) -> list[OfferDetails]:
        """
        :raises DataMapperError:
        """

    @abstractmethod
    async def get_offer_by_id(self, offer_id: Id) -> Offer | None:
        """
        :raises DataMapperError:
        """

    @abstractmethod
    async def get_full_offer_by_id(self, offer_id: Id) -> OfferDetails | None:
        """
        :raises DataMapperError:
        """
