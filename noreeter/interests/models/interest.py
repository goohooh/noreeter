from django.db import models


class Interest(models.Model):
    name = models.CharField(
        unique=True,
        max_length=20,
    )

    def __str__(self):
        return self.name
