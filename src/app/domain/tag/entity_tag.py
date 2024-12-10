from dataclasses import dataclass

from app.domain.base.entity import Entity
from app.domain.base.value_object import Id
from app.domain.tag.vo_tag import TagKey, TagValue


@dataclass(eq=False, kw_only=True)
class Tag(Entity[Id]):
    offer_id: Id
    key: TagKey
    value: TagValue
