from abc import abstractmethod
from typing import Protocol, List

from src.app.domain.base.value_object import Id
from src.app.domain.user.value_object import UserEmail
from src.app.domain.user_auth.entity import UserAuth


class AuthRepository(Protocol):
    @abstractmethod
    async def save(self, auth_user: UserAuth) -> None:
        """
        :raises DataMapperError:
        """

    @abstractmethod
    async def read_by_id(self, user_id: Id) -> UserAuth | None:
        """
        :raises DataMapperError:
        """

    @abstractmethod
    async def read_by_email(self, username: UserEmail) -> UserAuth | None:
        """
        :raises DataMapperError:
        """
