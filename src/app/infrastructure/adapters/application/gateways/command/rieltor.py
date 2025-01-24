from sqlalchemy.ext.asyncio import AsyncSession

from app.application.common.ports.gateways.command.rieltor import RieltorCommandGateway
from app.domain.rieltor.entity import Rieltor
from app.infrastructure.exceptions.gateways import DataMapperError

class RieltorCommandGatewayImpl(RieltorCommandGateway):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def save(self, rieltor: Rieltor) -> None:
        try:
            self._session.add(rieltor)
        except Exception as e:
            raise DataMapperError(f"Failed to save rieltor: {str(e)}")
