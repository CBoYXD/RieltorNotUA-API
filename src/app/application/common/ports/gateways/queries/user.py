from typing import Optional, Protocol
from abc import abstractmethod
from app.domain.base.value_object import Id
from app.domain.user.entity import User
from app.domain.user.value_object import UserEmail


class UserQueryRepository(Protocol):

    @abstractmethod
    async def read_by_id(self, user_id: Id) -> Optional[User]:
        """
        :raises DataMapperError:
        """

    @abstractmethod
    async def read_by_email(self, username: UserEmail) -> Optional[User]:
        """
        :raises DataMapperError:
        """
