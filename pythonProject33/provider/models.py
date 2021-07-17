from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from core.models import SoftDelete, CreatedAt, UpdateAt, Action
from core.enums import Carcase, State


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


class Car(SoftDelete, CreatedAt, UpdateAt):
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.PROTECT, related_name="cars"
    )
    model = models.CharField(max_length=50)
    carcase = models.CharField(max_length=25, choices=Carcase.choices())
    state = models.CharField(max_length=25, choices=State.choices())
    price = models.DecimalField(max_digits=10, decimal_places=2)
    production_date = models.DateTimeField()

    def __str__(self):
        return self.model


class Provider(SoftDelete, CreatedAt, UpdateAt):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True)
    foundation_time = models.DateTimeField()
    cars = models.ManyToManyField(Car, related_name="providers")
    customers = models.ManyToManyField(
        "car_dealerships.CarDealership",
        related_name="providers",
    )

    def __str__(self):
        return self.name


class ProviderAction(Action, SoftDelete, CreatedAt, UpdateAt):
    provider = models.ForeignKey(
        Provider,
        on_delete=models.CASCADE,
        related_name="actions",
    )
