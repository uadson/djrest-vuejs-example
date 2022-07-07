from django.contrib import admin

from api.models.breads import Bread


@admin.register(Bread)
class BreadAdmin(admin.ModelAdmin):
    pass
