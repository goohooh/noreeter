from django.db import models


class Town(models.Model):
    full_address = models.CharField(
        max_length=20,
        unique=True,
    )

    state = models.CharField(
        max_length=10,
    )

    city = models.CharField(
        max_length=8,
    )

    town_name = models.CharField(
        max_length=8,
    )
