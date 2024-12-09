from dataclasses import dataclass
from typing import Optional
from uuid import UUID

from app.domain.base.entity import Entity
from app.domain.offer.entity_offer import Offer
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
    offers: list[Offer] = []
