from abc import abstractmethod
from typing import Protocol

from app.domain.base.value_object import Id


class IdentityProvider(Protocol):
    @abstractmethod
    async def get_current_user_id(self) -> Id:
        """
        :raises AuthenticationError:
        """
