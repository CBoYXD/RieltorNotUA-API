from abc import abstractmethod
from typing import Protocol

from app.domain.base.value_object import Id


class AccessRevoker(Protocol):
    @abstractmethod
    async def remove_all_user_access(self, user_id: Id) -> None:
        """
        :raises DataMapperError:
        """
