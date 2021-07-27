from core.enums.base_enum import BaseEnum


class Carcase(BaseEnum):
    SEDAN = "sedan"
    HATCHBACK = "hatchback"
    COUPE = "coupe"
    CABRIOLET = "cabriolet"
    LIMOUSINE = "limousine"


class State(BaseEnum):
    NEW = "new"
    WITH_MILEAGE = "with mileage"
    BROKEN = "broken"
    TOTAL = "total"


class Engine(BaseEnum):
    PETROL = "petrol engine"
    DIESEL = "diesel engine"
    GAS = "gas engine"
    ELECTRIC = "electric engine"
