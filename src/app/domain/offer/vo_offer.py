from dataclasses import dataclass

from app.domain.base.value_object import ValueObject


@dataclass(frozen=True, repr=False)
class OfferArea:
    value: float


@dataclass(frozen=True, repr=False)
class OfferName:
    value: str


@dataclass(frozen=True, repr=False)
class OfferName:
    value: str


@dataclass(frozen=True, repr=False)
class OfferDescription:
    value: str
 

@dataclass(frozen=True, repr=False)
class OfferLocation:
    value: tuple[float, float]
    

@dataclass(frozen=True, repr=False)
class OfferPrice:
    value: int
    
    
@dataclass(frozen=True, repr=False)
class OfferFloor:
    value: int


@dataclass(frozen=True, repr=False)
class OfferPhoto:
    value: str
    

@dataclass(frozen=True, repr=False)
class OfferTag:
    value: str
