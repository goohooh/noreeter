from django.contrib.auth.models import AbstractUser
from django.db import models

from towns.models import Town


class User(AbstractUser):

    profile_image = models.ImageField(
        blank=True,
        null=True,
    )

    profile = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    town = models.ForeignKey(
        Town,
        blank=True,
        null=True,
    )
