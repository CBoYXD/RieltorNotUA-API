from dataclasses import dataclass

from app.domain.base.value_object import ValueObject
from app.domain.offer_details.validation.functions import validate_description


@dataclass(frozen=True, repr=False)
class OfferDetailsDescription(ValueObject):
    value: str

    def __post_init__(self) -> None:
        """
        :raises DomainFieldError:
        """
        super().__post_init__()

        validate_description(self.value)
