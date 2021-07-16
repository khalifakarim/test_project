from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from core.models import SoftDelete, CreatedAt, UpdateAt
from core.enums import Carcase, State


class Manufacturer(SoftDelete, CreatedAt, UpdateAt):
    description = models.TextField()
    name = models.CharField(max_length=150, unique=True)
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

    def __str__(self):
        return self.model


class Provider(SoftDelete, CreatedAt, UpdateAt):
    description = models.TextField()
    name = models.CharField(max_length=150, unique=True)
    foundation_time = models.DateTimeField()
    cars = models.ManyToManyField(Car)
    customers = models.ManyToManyField("car_dealerships.CarDealership")

    def __str__(self):
        return self.name


class ProviderAction(SoftDelete, CreatedAt, UpdateAt):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    cars = models.ManyToManyField(Car)
    provider = models.ForeignKey(
        Provider, on_delete=models.CASCADE, related_name="actions"
    )
    action_start_time = models.DateTimeField()
    action_end_time = models.DateTimeField()
    discount_percentage = models.IntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(100)]
    )

    def __str__(self):
        return self.title
