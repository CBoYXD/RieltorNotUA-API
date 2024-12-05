from dataclasses import dataclass
from typing import Self
from uuid import UUID

from app.domain.base.entity import Entity
from app.domain.user.enums import UserRole
from app.domain.user.vo_user import UserId, Username, UserPasswordHash


@dataclass(eq=False, kw_only=True)
class User(Entity[UserId]):
    username: Username
    password_hash: UserPasswordHash
    role: UserRole
    is_active: bool

    @classmethod
    def create(cls, *, user_id: UUID, username: str, password_hash: bytes, role: UserRole) -> Self:
        return cls(
            id_=UserId(user_id),
            username=Username(username),
            password_hash=UserPasswordHash(password_hash),
            role=role,
            is_active=True,
        )

    def activate(self) -> None:
        self.is_active = True

    def inactivate(self) -> None:
        self.is_active = False

    def grant_role(self, role: UserRole) -> None:
        self.role = role
