from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.application.common.ports.gateways.queries.user import UserQueryGateway
from app.domain.base.value_object import Id
from app.domain.user.entity import User
from app.domain.user.value_object import UserEmail
from app.domain.user_auth.entity import UserAuth
from app.infrastructure.exceptions.gateways import DataMapperError

class UserQueryGatewayImpl(UserQueryGateway):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def read_by_id(self, user_id: Id) -> Optional[User]:
        try:
            return await self._session.get_one(User, user_id)
        except Exception as e:
            raise DataMapperError(f"Failed to read user: {str(e)}")

    async def read_by_email(self, email: UserEmail) -> Optional[User]:
        try:
            result = await self._session.execute(
                select(User).filter(User.email == email)
            )
            return result.scalar_one_or_none()
        except Exception as e:
            raise DataMapperError(f"Failed to read user by email: {str(e)}")

    async def read_user_auth_by_email(self, email: UserEmail) -> Optional[UserAuth]:
        try:
            result = await self._session.execute(
                select(UserAuth).filter(UserAuth.email == email)
            )
            return result.scalar_one_or_none()
        except Exception as e:
            raise DataMapperError(f"Failed to read user auth: {str(e)}")
