from abc import abstractmethod
from typing import Protocol
from app.domain.offer_details.entity import OfferDetails


class OfferDetailsCommandGateway(Protocol):
    @abstractmethod
    async def save(self, offer_details: OfferDetails) -> None:
        """
        :raises DataMapperError:
        """
