from app.domain.base.exceptions import DomainFieldError
from app.domain.user_auth.exceptions import RawPasswordError
from app.domain.user_auth.validation.constants import PASSWORD_MIN_LEN


def validation_password_length(password_value: str) -> None:
    """
    :raises RawPasswordError:
    """
    password_len = len(password_value)
    if not PASSWORD_MIN_LEN <= password_len:
        raise RawPasswordError(password_len, PASSWORD_MIN_LEN)
