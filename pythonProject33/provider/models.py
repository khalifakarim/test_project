from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from core.abstract_models.base_abstract_models import (
    SoftDelete,
    CreatedAt,
    UpdateAt,
)
from core.abstract_models.abstract_models import Action
from core.enums.car import Carcase, State, Engine


class Manufacturer(SoftDelete, CreatedAt, UpdateAt):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True)
    location = models.ForeignKey(
        "car_dealerships.Location",
        on_delete=models.SET_NULL,
        null=True,
        related_name="+",
    )
    foundation_time = models.DateTimeField()

    def __str__(self):
        return self.name


class Car(SoftDelete, CreatedAt, UpdateAt):
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.PROTECT,
        related_name="cars",
    )
    model = models.CharField(max_length=50)
    carcase = models.CharField(max_length=13, choices=Carcase.choices())
    state = models.CharField(max_length=13, choices=State.choices())
    price = models.DecimalField(max_digits=10, decimal_places=2)
    production_year = models.IntegerField(
        validators=(MinValueValidator(1950), MaxValueValidator(2021))
    )
    type_of_engine = models.CharField(max_length=15, choices=Engine.choices())
    horse_power = models.IntegerField(
        validators=(MinValueValidator(50), MaxValueValidator(1600))
    )

    def __str__(self):
        return f'{self.manufacturer.name} - {self.model} - {self.carcase} - {self.state}'


class Provider(SoftDelete, CreatedAt, UpdateAt):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True)
    foundation_time = models.DateTimeField()
    cars = models.ManyToManyField(
        Car,
        through="CarPrice",
        through_fields=("provider", "car"),
        related_name="providers",
    )
    customers = models.ManyToManyField(
        "car_dealerships.CarDealership",
        related_name="providers",
    )

    def __str__(self):
        return self.name


class CarPrice(SoftDelete, CreatedAt, UpdateAt):
    provider = models.ForeignKey(
        Provider,
        related_name="prices",
        on_delete=models.CASCADE,
    )
    car = models.ForeignKey(
        Car,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.provider} - {self.car} - {self.price}'


class ProviderAction(Action, SoftDelete, CreatedAt, UpdateAt):
    provider = models.ForeignKey(
        Provider,
        on_delete=models.CASCADE,
        related_name="actions",
    )
