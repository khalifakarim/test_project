from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.db import models

from core.enums.customer import Gender
from provider.models import Car

from core.abstract_models.base_abstract_models import (
    SoftDelete,
    CreatedAt,
    UpdateAt,
)


class User(AbstractUser, SoftDelete, CreatedAt, UpdateAt):
    email = models.EmailField(max_length=150, unique=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    balance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        null=True
    )
    age = models.PositiveSmallIntegerField(
        validators=(MinValueValidator(18), MaxValueValidator(100)),
        null=True
    )
    gender = models.CharField(choices=Gender.choices(), max_length=6, null=True)
    birthday = models.DateTimeField(null=True,)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password", "username"]

    def __str__(self):
        return self.email


class Offer(SoftDelete, CreatedAt, UpdateAt):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="offers",
    )
    max_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name='+',
    )

    def __str__(self):
        return f"{self.car} , {self.max_price}"
