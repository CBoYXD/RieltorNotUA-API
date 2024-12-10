import re
from app.domain.base.exceptions import DomainFieldError

from app.domain.offer.validation.constants import (
    MIN_AREA_NUM,
    MAX_AREA_NUM,
    NAME_PATTERN,
    DESCRIPTION_MIN_LEN,
    DESCRIPTION_MAX_LEN,
    LOCATION_LATITUDE_MAX,
    LOCATION_LATITUDE_MIN,
    LOCATION_LONGITUDE_MAX,
    LOCATION_LONGITUDE_MIN,
    PRICE_MAX,
    PRICE_MIN,
    PHOTO_EXTENSTIONS,
    TAG_PATTERN
)


def validate_area(area_value: float) -> None:
    if not (MIN_AREA_NUM <= area_value <= MAX_AREA_NUM):
        raise DomainFieldError(
            f"Area must be between "
            f"{MIN_AREA_NUM} and "
            f"{MAX_AREA_NUM}."
        )


def validate_name(name_value: str) -> None:
    if not re.match(NAME_PATTERN, name_value):
        raise DomainFieldError("Cannot validate name.")

     
def validate_description(description_value: str) -> None:
    if not (DESCRIPTION_MIN_LEN <= len(description_value) <= DESCRIPTION_MAX_LEN):
        raise DomainFieldError(
            f"Description must be between "
            f"{DESCRIPTION_MIN_LEN} and "
            f"{DESCRIPTION_MAX_LEN} characters."
        )


def validate_latitude(latitude_value: float) -> None:
    if not (LOCATION_LATITUDE_MIN <= latitude_value <= LOCATION_LATITUDE_MAX):
        raise DomainFieldError(
            f"Latitude must be between "
            f"{LOCATION_LATITUDE_MIN} and "
            f"{LOCATION_LATITUDE_MAX}."
        )


def validate_longitude(longitude_value: float) -> None:
    if not (LOCATION_LONGITUDE_MIN <= longitude_value <= LOCATION_LONGITUDE_MAX):
        raise DomainFieldError(
            f"Longitude must be between "
            f"{LOCATION_LONGITUDE_MIN} and "
            f"{LOCATION_LONGITUDE_MAX}."
        )


def validate_price(price_value: int) -> None:
    if not (PRICE_MIN <= price_value <= PRICE_MAX):
        raise DomainFieldError(
            f"Price must be between "
            f"{PRICE_MIN} and "
            f"{PRICE_MAX}."
        )


def validate_photo(photo_value: str) -> None:
    if not photo_value.endswith(PHOTO_EXTENSTIONS):
        raise DomainFieldError(
            f"Photo must be in {', '.join(PHOTO_EXTENSTIONS)}."
        )


def validate_tag(tag_value: str) -> None:
    if not re.match(TAG_PATTERN, tag_value):
        raise DomainFieldError("Cannot validate tag.")
