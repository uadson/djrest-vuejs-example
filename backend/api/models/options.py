from django.db import models

from api.models.base import Base


class Option(Base):
    name = models.CharField('Optional', max_length=50)

    class Meta:
        verbose_name = 'Option'
        verbose_name_plural = 'Optional'
        db_table = 'option'

    def __str__(self):
        return self.name
