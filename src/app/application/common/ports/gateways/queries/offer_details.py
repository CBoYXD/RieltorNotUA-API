from typing import Optional, Protocol
from abc import abstractmethod
from app.domain.base.value_object import Id
from app.domain.offer_details.entity import OfferDetails


class OfferDetailsQueryRepository(Protocol):
    @abstractmethod
    async def read_by_id(self, offer_details_id: Id) -> Optional[OfferDetails]:
        """
        :raises DataMapperError:
        """
