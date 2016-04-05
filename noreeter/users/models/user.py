from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    profile_image = models.ImageField()

    profile = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
