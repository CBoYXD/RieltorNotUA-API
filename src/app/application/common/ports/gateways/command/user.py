from typing import Protocol
from abc import abstractmethod
from app.domain.user.entity import User


class UserCommandRepository(Protocol):
    @abstractmethod
    async def save(self, user: User) -> None:
        """
        :raises DataMapperError:
        """
