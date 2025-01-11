from typing import Optional, Protocol, List
from abc import abstractmethod
from app.domain.base.value_object import Id
from app.domain.offer.entity import Offer
from app.domain.offer_details.entity import OfferDetails


class OfferQueryGateway(Protocol):
    @abstractmethod
    async def read_by_id(self, offer_id: Id) -> Optional[Offer]:
        """
        :raises DataMapperError:
        """

    @abstractmethod
    async def read_all(self) -> List[Offer]:
        """
        :raises DataMapperError:
        """

    @abstractmethod
    async def read_full_offer_by_id(self, offer_id: Id) -> Optional[OfferDetails]:
        """
        :raises DataMapperError:
        """

    @abstractmethod
    async def read_all_full_offers(self) -> List[OfferDetails]:
        """
        :raises DataMapperError:
        """
