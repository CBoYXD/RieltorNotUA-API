from app.domain.base.exceptions import DomainFieldError
from app.domain.offer.validation.constants import (
    DESCRIPTION_MAX_LEN,
    DESCRIPTION_MIN_LEN,
)


def validate_description(description_value: str) -> None:
    if not (DESCRIPTION_MIN_LEN <= len(description_value) <= DESCRIPTION_MAX_LEN):
        raise DomainFieldError(
            f'Description must be between '
            f'{DESCRIPTION_MIN_LEN} and '
            f'{DESCRIPTION_MAX_LEN} characters.'
        )
