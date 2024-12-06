from dataclasses import dataclass
from typing import Optional
from uuid import UUID

from app.domain.base.entity import Entity
from app.domain.base.value_object import Id
from app.domain.user.enums import UserRole
from app.domain.user.vo_user import UserFullname, UserEmail, UserName


@dataclass(eq=False, kw_only=True)
class User(Entity[Id]):
    email: UserEmail
    username: UserName
    full_name: UserFullname
    role: UserRole
    is_active: bool

    @classmethod
    def create(
        cls, *, user_id: UUID, email: str, 
        full_name: str, role: UserRole, username: str
    ) -> User:
        return cls(
            id_=Id(user_id),
            username=UserName(username),
            email=UserEmail(email),
            full_name=UserFullname(full_name),
            role=role,
            is_active=True,
        )

    def activate(self) -> None:
        self.is_active = True

    def inactivate(self) -> None:
        self.is_active = False

    def grant_role(self, role: UserRole) -> None:
        self.role = role
