from django.apps import AppConfig


class CarDealershipsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "car_dealerships"

    def ready(self):
        import car_dealerships.signals
