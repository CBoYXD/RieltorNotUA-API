from typing import Optional, Protocol
from abc import abstractmethod
from app.domain.base.value_object import Id
from app.domain.rieltor.entity import Rieltor


class RieltorQueryGateway(Protocol):
    @abstractmethod
    async def read_by_id(self, rieltor_id: Id) -> Optional[Rieltor]:
        """
        :raises DataMapperError:
        """

    @abstractmethod
    async def read_by_email(self, email: UserEmail) -> Optional[Rieltor]:
        """
        :raises DataMapperError:
        """
