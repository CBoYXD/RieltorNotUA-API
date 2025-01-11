from abc import abstractmethod
from typing import Protocol
from app.domain.user_auth.entity import UserAuth


class UserAuthCommandRepository(Protocol):
    @abstractmethod
    async def save(self, auth_user: UserAuth) -> None:
        """
        :raises DataMapperError:
        """
