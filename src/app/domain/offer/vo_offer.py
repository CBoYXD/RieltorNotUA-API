from dataclasses import dataclass

from app.domain.offer.validation.functions import (
    validate_area,
    validate_name,
    validate_price,
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
class OfferPrice:
    value: int

    def __post_init__(self) -> None:
        """
        :raises DomainFieldError:
        """
        super().__post_init__()

        validate_price(self.value)
