from uuid import UUID, uuid4

from app.domain.base.ports.uuid_generator import UUIDGenerator


class AdapterUUIDGenerator(UUIDGenerator):
    def __call__(self) -> UUID:        
        return uuid4()
