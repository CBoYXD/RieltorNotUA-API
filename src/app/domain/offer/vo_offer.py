from dataclasses import dataclass

from app.domain.base.value_object import ValueObject
from app.domain.offer.validation.functions import (
    validate_area,
    validate_name,
    validate_description,
    validate_latitude,
    validate_longitude,
    validate_price,
    validate_photo,
    validate_tag,
    validate_floor
)


@dataclass(frozen=True, repr=False)
class OfferArea:
    value: float

    def __post_init__(self) -> None:
        """
        :raises DomainFieldError:
        """
        super().__post_init__()

        validate_area(self.value)


@dataclass(frozen=True, repr=False)
class OfferName:
    value: str
    
    def __post_init__(self) -> None:
        """
        :raises DomainFieldError:
        """
        super().__post_init__()

        validate_name(self.value)


@dataclass(frozen=True, repr=False)
class OfferDescription:
    value: str
    
    def __post_init__(self) -> None:
        """
        :raises DomainFieldError:
        """
        super().__post_init__()

        validate_description(self.value)
 

@dataclass(frozen=True, repr=False)
class OfferLocation:
    latitude: float
    longitude: float
    
    def __post_init__(self) -> None:
        """
        :raises DomainFieldError:
        """
        super().__post_init__()

        validate_latitude(self.latitude)
        validate_longitude(self.longitude)
    

@dataclass(frozen=True, repr=False)
class OfferPrice:
    value: int
    
    def __post_init__(self) -> None:
        """
        :raises DomainFieldError:
        """
        super().__post_init__()

        validate_price(self.value)
    

@dataclass(frozen=True, repr=False)
class OfferPhoto:
    value: str
    
    def __post_init__(self) -> None:
        """
        :raises DomainFieldError:
        """
        super().__post_init__()

        validate_photo(self.value)
    

@dataclass(frozen=True, repr=False)
class OfferTag:
    value: str
    
    def __post_init__(self) -> None:
        """
        :raises DomainFieldError:
        """
        super().__post_init__()

        validate_tag(self.value)


@dataclass(frozen=True, repr=False)
class OfferFloor:
    value: int
    
    def __post_init__(self) -> None:
        """
        :raises DomainFieldError:
        """
        super().__post_init__()

        validate_floor(self.value)
