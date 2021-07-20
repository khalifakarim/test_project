from enum import Enum


class BaseEnum(Enum):
    @classmethod
    def choices(cls):
        return [(value.name, value.value) for value in cls]
