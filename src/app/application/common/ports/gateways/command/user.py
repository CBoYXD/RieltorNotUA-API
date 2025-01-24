from typing import Protocol
from abc import abstractmethod
from app.domain.user.entity import User
from app.domain.user_auth.entity import UserAuth


class UserCommandGateway(Protocol):
    @abstractmethod
    async def save(self, user: User) -> None:
        """
        :raises DataMapperError:
        """

    @abstractmethod
    async def save_user_auth(self, user: UserAuth) -> None:
        """
        :raises DataMapperError:
        """
