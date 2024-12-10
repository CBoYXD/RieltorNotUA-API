import re

# Area validation
MIN_AREA_NUM: int = 0
MAX_AREA_NUM: int = 10000

# Name validation
NAME_PATTERN: str = r'^[A-Za-zА-Яа-яіІїЇєЄє]+(?: [A-Za-zА-Яа-яіІїЇєЄє]+)*$'

# Description validation
DESCRIPTION_MIN_LEN: int = 10
DESCRIPTION_MAX_LEN: int = 200

# Location validation
LOCATION_LATITUDE_MIN: int = -90.0
LOCATION_LATITUDE_MAX: int = 90.0
LOCATION_LONGITUDE_MIN: int = -180.0
LOCATION_LONGITUDE_MAX: int = 180.0

# Price validation
PRICE_MIN: int = 500
PRICE_MAX: int = 1000000000000

# Photo validation
PHOTO_EXTENSTIONS: list[str] = [".jpg", ".png", ".jpeg"]

# Tag validation
TAG_PATTERN: str = r'^[A-Za-z]{3,10}$'
