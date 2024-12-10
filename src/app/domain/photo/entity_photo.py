from dataclasses import dataclass

from app.domain.base.entity import Entity
from app.domain.base.value_object import Id
from app.domain.photo.vo_photo import PhotoExtenstion, PhotoName


@dataclass(eq=False, kw_only=True)
class Photo(Entity[Id]):
    offer_id: Id
    extenstion: PhotoExtenstion
    name: PhotoName
