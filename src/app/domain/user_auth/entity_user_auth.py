from dataclasses import dataclass

from app.domain.user.entity_user import User
from app.domain.user_auth.vo_user_auth import UserPasswordHash


@dataclass(eq=False, kw_only=True)
class UserAuth(User):
    password: UserPasswordHash
