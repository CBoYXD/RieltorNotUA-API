from abc import abstractmethod
from uuid import UUID


class UUIDGenerator:
    @abstractmethod
    def __call__(self) -> UUID: ...
