from django.contrib import admin

from api.models.breads import Bread

from datetime import datetime


@admin.register(Bread)
class BreadAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        '_created',
        '_updated',
        'active',
    )
    exclude = ['created', 'updated', ]

    def _created(self, instance):
        return instance.created.strftime('%d/%m/%Y, %H:%M')

    def _updated(self, instance):
        return instance.updated.strftime('%d/%m/%Y, %H:%M')
