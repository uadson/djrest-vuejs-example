from django.db import models

from .base import Base


class Meat(Base):
    name = models.CharField('Name', max_length=150)

    class Meta:
        verbose_name = 'Meat'
        verbose_name_plural = 'Meats'
        db_table = 'meat'

    def __str__(self):
        return self.name
