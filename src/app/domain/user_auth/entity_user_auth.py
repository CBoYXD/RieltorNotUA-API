from dataclasses import dataclass
from uuid import UUID

from app.domain.user.entity_user import User
from app.domain.user.vo_user import UserId, UserEmail, UserFullname
from app.domain.user_auth.vo_user_auth import UserPasswordHash


@dataclass(eq=False, kw_only=True)
class UserAuth(User):
    password: UserPasswordHash

    @classmethod
    def create(cls, password: str, **kwargs) -> UserAuth:
        return cls(password=password, **super().create(**kwargs))
