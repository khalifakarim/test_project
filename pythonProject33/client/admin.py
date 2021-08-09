from django.contrib import admin

from client.models import User, Offer, RegularClient


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "username", "balance")
    list_filter = (
        "email",
        "username",
    )
    search_fields = (
        "email",
        "username",
    )


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ("user", "car", "max_price")
    list_filter = ("car__model", "car__state")
    search_fields = (
        "title",
        "car__model",
        "car_showroom__name",
        "car__manufacturer__name",
        "user__mail",
    )


@admin.register(RegularClient)
class RegularClientAdmin(admin.ModelAdmin):
    list_display = (
        "client",
        "purchase_amount",
        "discount_percentage",
        "car_dealership",
    )
    search_fields = (
        "car_dealership__name",
        "client__mail",
    )
    ordering = (
        "-discount_percentage",
        '-purchase_amount',
    )
