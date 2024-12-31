from dataclasses import dataclass

from app.domain.base.entity import Entity
from app.domain.base.value_object import Id
from app.domain.photo.vo_photo import PhotoExtenstion, PhotoName


@dataclass(eq=False, kw_only=True)
class Photo(Entity[Id]):
    offer_id: Id
    extenstion: PhotoExtenstion
    name: PhotoName

    def create(
        id_generator: UUIDGenerator,
        offer_id: Id,
        extension: str,
        name: str
    ) -> Photo:
        return Photo(
            id_=Id(id_generator()),
            offer_id=offer_id,
            extenstion=PhotoExtenstion(extension),
            name=PhotoName(name)
        )
