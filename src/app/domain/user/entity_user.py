from typing import List

from dataclasses import dataclass, field

from src.app.domain.base.entity import Entity
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

