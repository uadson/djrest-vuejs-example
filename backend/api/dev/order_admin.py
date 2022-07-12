from django.contrib import admin

from api.models.order import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
