from enum import Enum


class OfferType(Enum):
    SALE = 'sale'
    RENT = 'rent'


class OfferPlaceType(Enum):
    HOUSE = 'house'
    FLAT = 'flat'
    OFFICE = 'office'
