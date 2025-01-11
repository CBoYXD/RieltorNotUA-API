from abc import abstractmethod
from typing import Protocol
from app.domain.offer.entity import Offer


class OfferCommandGateway(Protocol):
    @abstractmethod
    async def save(self, offer: Offer) -> None:
        """
        :raises DataMapperError:
        """
