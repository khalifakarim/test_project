from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.base_user import BaseUserManager
from django.db import models

from core.enums.customer import Gender
from provider.models import Car

from core.abstract_models.base_abstract_models import (
    SoftDelete,
    CreatedAt,
    UpdateAt,
)


class UserManager(BaseUserManager):

    def _create_user(self, **kwargs):
        user = self.model(**kwargs)
        user.set_password(kwargs.get('password'))
        user.save(using=self._db)
        return user

    def create_user(self, **kwargs):
        kwargs['is_active'] = True
        return self._create_user(**kwargs)

    def create_superuser(self, **kwargs):
        kwargs.setdefault('is_active', True)
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        return self._create_user(**kwargs)


class User(AbstractBaseUser, PermissionsMixin, SoftDelete, CreatedAt, UpdateAt):
    email = models.EmailField(max_length=150, unique=True)
    username = models.CharField(max_length=50)
    balance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )
    age = models.PositiveSmallIntegerField(
        validators=(MinValueValidator(18), MaxValueValidator(100)),
    )
    gender = models.CharField(choices=Gender.choices(), max_length=6)
    birthday = models.DateTimeField(null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "password",
        "username",
        "age",
        "gender",
    ]

    objects = UserManager()

    def __str__(self):
        return self.email


class OfferManager(models.Manager):
    def get_active_offers(self):
        return super().get_queryset().filter(is_active=True)

    def check_user_offer(self, user_id):
        return super().get_queryset().filter(is_active=True, user__id=user_id)


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

    objects = OfferManager()
