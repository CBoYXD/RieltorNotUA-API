from sqlalchemy.ext.asyncio import AsyncSession

from app.application.common.ports.gateways.command.user import UserCommandGateway
from app.domain.user.entity import User
from app.domain.user_auth.entity import UserAuth
from app.infrastructure.exceptions.gateways import DataMapperError

class UserCommandGatewayImpl(UserCommandGateway):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def save(self, user: User) -> None:
        try:
            self._session.add(user)
        except Exception as e:
            raise DataMapperError(f"Failed to save user: {str(e)}")

    async def save_user_auth(self, user_auth: UserAuth) -> None:
        try:
            self._session.add(user_auth)
        except Exception as e:
            raise DataMapperError(f"Failed to save user auth: {str(e)}")
