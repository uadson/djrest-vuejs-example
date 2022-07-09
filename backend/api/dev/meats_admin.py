from django.contrib import admin

from api.models.meats import Meat


@admin.register(Meat)
class MeatAdmin(admin.ModelAdmin):
    pass
