from abc import abstractmethod
from typing import Protocol, List

from src.app.domain.base.value_object import Id
from src.app.domain.user.vo_user import UserEmail
from src.app.domain.user_auth.entity_user_auth import UserAuth


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
    async def read_by_email(
            self, username: UserEmail, for_update: bool = False
    ) -> UserAuth | None:
        """
        :raises DataMapperError:
        """


    @abstractmethod
    async def read_all(self, limit: int, offset: int) -> List[UserAuth]:
        """
        :raises DataMapperError:
        """