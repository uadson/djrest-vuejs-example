from django.db import models

from .base import Base


class Bread(Base):
    name = models.CharField('Name', max_length=100)

    class Meta:
        verbose_name = 'Bread'
        verbose_name_plural = 'Breads'
        db_table = 'bread'

    def __str__(self):
        return self.name
