from typing import Protocol
from abc import abstractmethod
from app.domain.user.entity import User


class UserCommandGateway(Protocol):
    @abstractmethod
    async def save(self, user: User) -> None:
        """
        :raises DataMapperError:
        """
