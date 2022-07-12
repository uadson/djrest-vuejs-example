from django.db import models

from api.models.base import Base
from api.models.breads import Bread
from api.models.meats import Meat


class Order(Base):
    STATUS_CHOICES = (
        ('Solicitado', 'Solicitado'),
        ('Em Produção', 'Em Produção'),
        ('Finalizado', 'Finalizado')
    )
    customer = models.CharField('Customer', max_length=200)
    bread = models.ForeignKey(Bread, on_delete=models.CASCADE)
    meat = models.ForeignKey(Meat, on_delete=models.CASCADE)
    status = models.CharField(
        'Status', choices=STATUS_CHOICES, default='Solicitado', max_length=11)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        db_table = 'order'

    def __str__(self):
        return f'Order n.: {self.id}'
