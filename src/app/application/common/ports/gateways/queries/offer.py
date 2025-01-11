from typing import Optional, Protocol
from abc import abstractmethod
from app.domain.base.value_object import Id
from app.domain.offer.entity import Offer


class OfferQueryGateway(Protocol):
    @abstractmethod
    async def read_by_id(self, offer_id: Id) -> Optional[Offer]:
        """
        :raises DataMapperError:
        """
