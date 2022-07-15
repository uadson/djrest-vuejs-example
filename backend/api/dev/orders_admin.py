from django.contrib import admin

from api.models.orders import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'customer',
        'bread',
        'meat',
        'status',
        '_created',
        '_updated',
    )

    exclude = ['created', 'updated', ]

    def _created(self, instance):
        return instance.created.strftime('%d/%m/%Y, %H:%M')

    def _updated(self, instance):
        return instance.updated.strftime('%d/%m/%Y, %H:%M')
