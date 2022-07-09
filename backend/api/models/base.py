from django.db import models


class Base(models.Model):
    created = models.DateTimeField('Created', auto_now_add=True)
    updated = models.DateTimeField('Updated', auto_now=True)
    active = models.BooleanField('Active', default=True)

    class Meta:
        abstract = True