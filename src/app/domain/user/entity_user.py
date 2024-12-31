from typing import List

from dataclasses import dataclass, field

from src.app.domain.base.entity import Entity
from src.app.domain.base.ports.uuid_generator import UUIDGenerator
from src.app.domain.base.value_object import Id
from src.app.domain.offer.entity_offer import Offer
from src.app.domain.user.enums import UserRole
from src.app.domain.user.vo_user import UserEmail, UserFullname, UserName


@dataclass(eq=False, kw_only=True)
class User(Entity[Id]):
    email: UserEmail
    username: UserName
    full_name: UserFullname
    role: UserRole
    is_active: bool
    
    
    def create(
        id_generator: UUIDGenerator, email: str, username: str,
        full_name: str, role: UserRole, is_active: bool
    ) -> User:
        return User(
            id_=Id(UUIDGenerator()()),
            email=UserEmail(email),
            username=UserName(username),
            full_name=UserFullname(full_name),
            role=role,
            is_active=is_active
        )

    def deactivate(self) -> None:
        self.is_active = False

    def change_role(self, new_role: UserRole) -> None:
        self.role = new_role

    def update_full_name(self, new_full_name: str) -> None:
        self.full_name = UserFullname(new_full_name)
