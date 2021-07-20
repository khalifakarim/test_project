from django.contrib import admin

from client.models import User, Offer


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "username", "balance")
    list_filter = (
        "email",
        "username",
        "is_active"
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
