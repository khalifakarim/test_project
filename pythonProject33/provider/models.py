from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from core.abstract_models.abstract_models import BaseCarRelation
from core.abstract_models.abstract_models import Action
from core.enums.car import Carcase, State, Engine

from core.abstract_models.base_abstract_models import (
    SoftDelete,
    CreatedAt,
    UpdateAt,
)


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
    customers = models.ManyToManyField(
        "car_dealerships.CarDealership",
        through='RegularProviderCustomers',
        through_fields=("provider", "customer"),
        related_name="providers",
    )

    def __str__(self):
        return self.name


class RegularProviderCustomers(SoftDelete, CreatedAt, UpdateAt):
    provider = models.ForeignKey(
        Provider,
        on_delete=models.CASCADE,
        related_name='regular_customers',
        related_query_name='regular_car_dealership',
    )
    customer = models.ForeignKey('car_dealerships.CarDealership', on_delete=models.CASCADE, related_name="promotions")
    discount_percentage = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )
    purchase_amount = models.PositiveSmallIntegerField()


class CarPrice(SoftDelete, CreatedAt, UpdateAt, BaseCarRelation):
    provider = models.ForeignKey(
        Provider,
        related_name="cars",
        related_query_name='car',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.provider} - {self.car} - {self.price}'


class ProviderAction(Action, SoftDelete, CreatedAt, UpdateAt):
    provider = models.ForeignKey(
        Provider,
        on_delete=models.CASCADE,
        related_name="actions",
    )

    def __str__(self):
        return f'{self.provider} - {self.title} - {self.action_start_time} - {self.action_end_time}'
