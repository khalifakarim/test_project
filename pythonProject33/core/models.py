from django.db import models


class SoftDelete(models.Model):
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class CreatedAt(models.Model):
    creation_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class UpdateAt(models.Model):
    modification_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
