from django.contrib import admin

from api.models.orders import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
