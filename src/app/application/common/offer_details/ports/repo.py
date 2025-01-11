from abc import abstractmethod
from typing import Protocol, List

from app.domain.base.value_object import Id
from app.domain.offer_details.entity import OfferDetails


class OfferDetailsRepository(Protocol):

    @abstractmethod
    async def get_all_offers(self, limit: int = None) -> list[OfferDetails]:
        """
        :raises DataMapperError:
        """

    @abstractmethod
    async def get_full_offer_by_id(self, offer_id: Id) -> OfferDetails | None:
        """
        :raises DataMapperError:
        """
