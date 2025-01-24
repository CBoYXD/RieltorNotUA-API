from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.application.common.ports.gateways.queries.rieltor import RieltorQueryGateway
from app.domain.base.value_object import Id
from app.domain.rieltor.entity import Rieltor
from app.domain.user.value_object import UserEmail
from app.infrastructure.exceptions.gateways import DataMapperError

class RieltorQueryGatewayImpl(RieltorQueryGateway):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def read_by_id(self, rieltor_id: Id) -> Optional[Rieltor]:
        try:
            return await self._session.get_one(Rieltor, rieltor_id)
        except Exception as e:
            raise DataMapperError(f"Failed to read rieltor: {str(e)}")

    async def read_by_email(self, email: UserEmail) -> Optional[Rieltor]:
        try:
            result = await self._session.execute(
                select(Rieltor).filter(Rieltor.email == email)
            )
            return result.scalar_one_or_none()
        except Exception as e:
            raise DataMapperError(f"Failed to read rieltor by email: {str(e)}")
