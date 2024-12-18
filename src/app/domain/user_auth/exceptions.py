from datetime import datetime


from src.app.domain.base.exceptions import DomainFieldError


class TimestampError(DomainFieldError):
    """
    Exception thrown for invalid time values.

    This exception occurs if the passed time value (e.g., `created_at` or `updated_at`)
    is in the future, which contradicts business logic invariants.

    Example:
        >>> raise TimestampError("created_at", datetime(2025, 1, 1))
        TimestampError: created_at '2025-01-01 00:00:00' cannot be in the future.
    """
    def __init__(self, field_name: str, time: datetime):
        """
        :param field_name: The name of the field for which the error occurred.
        :param time: An invalid time value.
        """
        message: str = f"{field_name} '{time}' cannot be in the future."
        super().__init__(message)


class RawPasswordError(DomainFieldError):
    """
    Exception thrown if the password length is invalid.

    This exception occurs if the password length is less than the minimum acceptable value.
    Typically used when validating user input in a domain.

    Example:
        >>> raise RawPasswordError(5, 8)
        RawPasswordError: Password must be at least 8 characters long. Got - 5
    """
    def __init__(self, password_len: int , min_len: int):
        message: str = f"Password must be at least {min_len} characters long. Got - {password_len}"
        super().__init__(message)