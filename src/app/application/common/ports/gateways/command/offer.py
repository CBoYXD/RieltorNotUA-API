from abc import abstractmethod
from typing import Protocol
from app.domain.base.value_object import Id
from app.domain.offer.entity import Offer
from app.domain.offer_details.entity import OfferDetails

class OfferCommandGateway(Protocol):
    @abstractmethod
    async def save(self, offer: Offer) -> None:
        """
        :raises DataMapperError:
        """
        
    @abstractmethod
    async def save_details(self, offer_details: OfferDetails) -> None:
        """
        :raises DataMapperError:
        """

    @abstractmethod
    async def delete(self, offer_id: Id) -> None:
        """
        :raises DataMapperError:
        """

    @abstractmethod
    async def delete_all(self, user_id: Id) -> None:
        """
        :raises DataMapperError:
        """
