from django.db import models


class SoftDeleteManager(models.Manager):

    def get_active_instances(self):
        return super().get_queryset().filter(is_active=True)
