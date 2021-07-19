from enum import Enum


class BaseEnum(Enum):
    @classmethod
    def choices(cls):
        return [(value.name, value.value) for value in cls]


class Carcase(BaseEnum):
    SEDAN = "sedan"
    HATCHBACK = "hatchback"
    COUPE = "coupe"
    CABRIOLET = "cabriolet"
    LIMOUSINE = "limousine"


class State(BaseEnum):
    NEW = "NEW"
    WITH_MILEAGE = "with mileage"
    BROKEN = "broken"
    TOTAL = "total"


class Engine(BaseEnum):
    PETROL = "petrol engine"
    DIESEL = "diesel engine"
    GAS = "gas engine"
    ELECTRIC = "electric engine"
