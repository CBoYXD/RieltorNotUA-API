from app.domain.base.exceptions import DomainFieldError
from app.domain.offer_details.validation.constants import (
    DESCRIPTION_MAX_LEN,
    DESCRIPTION_MIN_LEN,
    TAG_MIN_LEN,
    TAG_MAX_LEN
)


def validate_description(description_value: str) -> None:
    if not (DESCRIPTION_MIN_LEN <= len(description_value) <= DESCRIPTION_MAX_LEN):
        raise DomainFieldError(
            f'Description must be between '
            f'{DESCRIPTION_MIN_LEN} and '
            f'{DESCRIPTION_MAX_LEN} characters.'
        )

def validate_tag(tag_value: str) -> None:
    if not tag_value.startswith('#'):
        raise DomainFieldError('Tag must start with "#".')
    if not (TAG_MIN_LEN <= len(tag_value) <= TAG_MAX_LEN):
        raise DomainFieldError(
            f'Tag must be between '
            f'{TAG_MIN_LEN} and '
            f'{TAG_MAX_LEN} characters.'
        )
