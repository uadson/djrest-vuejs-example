from django.db import models
from django.utils import timezone

from datetime import datetime


class Base(models.Model):
    created = models.DateTimeField('Created', default=timezone.now)
    updated = models.DateTimeField('Updated', default=timezone.now)
    active = models.BooleanField('Active', default=True)

    class Meta:
        abstract = True
