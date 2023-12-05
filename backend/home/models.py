from django.conf import settings
from django.db import models


class D1(models.Model):
    "Generated Model"
    t1 = models.BigIntegerField()
    t2 = models.BigIntegerField(
        null=True,
        blank=True,
    )
