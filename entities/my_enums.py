from enum import Enum

class Hotel(Enum):
        CITY_HOTEL = 1
        RESORT_HOTEL = 2

class Meal(Enum):
    SC = 1
    BB = 2
    FB = 3
    HB = 4

class Distribution_channel (Enum):
    CORPORATE = 1
    DIRECT = 2
    GDS = 3
    TA_TO = 4

class Deposit_type(Enum):
    NO_DEPOSIT = 1
    NON_REFUND = 2
    REFUNDABLE = 3