import logging

from app.application.common.exceptions.auth import AuthorizationError
from app.application.common.ports.gateways.queries.user import UserQueryGateway
from app.application.common.ports.identity_provider import IdentityProvider
from app.domain.user.entity import User
from app.domain.user.enums import UserRole
from app.domain.base.value_object import Id

log = logging.getLogger(__name__)


class AuthService:
    def __init__(
        self,
        identity_provider: IdentityProvider,
        user_query_gateway: UserQueryGateway,
    ):
        self._identity_provider = identity_provider
        self._user_query_gateway = user_query_gateway
        self._current_user: User | None = None

    async def _get_current_user(self) -> User:
        """
        :raises AuthenticationError:
        :raises DataMapperError:
        :raises AuthorizationError:
        """
        if self._current_user is None:
            current_user_id: Id = (
                await self._identity_provider.get_current_user_id()
            )
            current_user: User | None = await self._user_query_gateway.read_by_id(
                current_user_id
            )
            if current_user is None:
                log.debug("Failed to retrieve current user.")
                raise AuthorizationError("Not authorized.")
            self._current_user = current_user
        return self._current_user

    async def authorize_action(self, permission_required: UserRole = UserRole.USER) -> None:
        """
        :raises AuthenticationError:
        :raises DataMapperError:
        :raises AuthorizationError:
        """
        current_user: User = await self._get_current_user()

        if current_user.role == UserRole.ADMIN:
            return

        elif current_user.role != permission_required:
            log.debug(
                "User '%s' lacks permission '%s'.",
                current_user.id_,
                permission_required,
            )
            raise AuthorizationError("Not authorized.")
