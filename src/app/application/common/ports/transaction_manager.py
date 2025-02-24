from abc import abstractmethod
from typing import Protocol


class TransactionManager(Protocol):
    """
    Transaction Manager is an UOW-compatible interface for
    flushing and committing changes to the data source.
    The actual implementation of UOW can be bundled with an ORM,
    like SQLAlchemy's session.
    """

    @abstractmethod
    async def commit(self) -> None:
        """
        :raise  DataMapperError:
        """

    
    @abstractmethod
    async def flush(self) -> None:
        """
        :raises DataMapperError:

        Mostly to check data source constraints.
        """
