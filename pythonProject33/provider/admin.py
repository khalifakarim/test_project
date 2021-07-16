from django.contrib import admin

from .models import Car, Provider, ProviderAction, Manufacturer


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        "model",
        "carcase",
        "state",
        "manufacturer__name",
        "price",
    )
    list_filter = (
        "manufacturer__name",
        "model",
    )
    search_fields = (
        "manufacturer",
        "model",
    )


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = (
        "description",
        "name",
        "foundation_time",
    )
    list_filter = (
        "cars",
        "is_active",
        "customers",
    )
    search_fields = (
        "name",
        "cars__model",
        "cars__state",
        "cars__manufacturer__name",
    )


@admin.register(ProviderAction)
class ProviderActionAdmin(admin.ModelAdmin):
    list_display = (
        "provider",
        "title",
        "description",
        "action_start_time",
        "action_end_time",
        "discount_percentage",
    )
    list_filter = (
        "cars",
        "is_active",
        "provider",
    )
    search_fields = (
        "title",
        "cars__model",
        "cars__manufacturer__name"
        "provider__name",
    )


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = (
        "description",
        "name",
        "location",
        "foundation_time",
    )
    list_filter = ("is_active",)
    search_fields = ("name",)
