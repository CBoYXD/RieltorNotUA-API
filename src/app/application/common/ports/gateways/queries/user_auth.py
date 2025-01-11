from typing import Optional, Protocol
from abc import abstractmethod
from app.domain.base.value_object import Id
from app.domain.user.value_object import UserEmail
from app.domain.user_auth.entity import UserAuth


class UserAuthQueryRepository(Protocol):

    @abstractmethod
    async def read_by_id(self, user_id: Id) -> Optional[UserAuth]:
        """
        :raises DataMapperError:
        """

    @abstractmethod
    async def read_by_email(self, username: UserEmail) -> Optional[UserAuth]:
        """
        :raises DataMapperError:
        """
