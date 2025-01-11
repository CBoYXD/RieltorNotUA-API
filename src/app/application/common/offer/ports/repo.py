from abc import abstractmethod
from typing import Protocol, List

from app.domain.base.value_object import Id
from app.domain.offer.entity import Offer


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
    async def get_offer_by_id(self, offer_id: Id) -> Offer | None:
        """
        :raises DataMapperError:
        """
