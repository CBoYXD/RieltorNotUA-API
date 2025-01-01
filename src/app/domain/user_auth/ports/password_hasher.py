from abc import abstractmethod
from typing import Protocol

from app.domain.user_auth.vo_user_auth import RawPassword


class PasswordHasher(Protocol):
    @abstractmethod
    def hash(self, raw_password: RawPassword) -> str: ...


    @abstractmethod
    def verify_password(self, raw_password: RawPassword, hashed_password: str) -> bool: ...


