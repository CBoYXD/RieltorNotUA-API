from abc import abstractmethod
from typing import Protocol
from app.domain.rieltor.entity import Rieltor


class RieltorCommandGateway(Protocol):
    @abstractmethod
    async def save(self, rieltor: Rieltor) -> None:
        """
        :raises DataMapperError:
        """
