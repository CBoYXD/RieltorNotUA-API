from dataclasses import dataclass

from app.domain.base.value_object import ValueObject
from app.domain.user.validation.functions import (
    validate_password_length,
    validate_username_length,
    validate_username_pattern,
    validate_user_email
)


@dataclass(frozen=True, repr=False)
class UserFullname(ValueObject):
    value: str
    # TODO: Add validation


@dataclass
class UserEmail:
    value: str
    
    def __post_init__(self) -> None:
        """
        :raises DomainFieldError:
        """
        super().__post_init__()

        validate_user_email(self.value)


@dataclass
class UserName:
    value: str
    
    def __post_init__(self) -> None:
        """
        :raises DomainFieldError:
        """
        super().__post_init__()

        validate_username_length(self.value)
        validate_username_pattern(self.value)
