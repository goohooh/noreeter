from django.conf import settings
from django.db import models


class Interest(models.Model):
    name = models.CharField(
        unique=True,
        max_length=20,
    )

    user_set = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="interest_set",
    )

    def __str__(self):
        return self.name
