from django.contrib.auth.models import AbstractUser
from django.db import models

from towns.models import Town


def generate_filename(self, filename):
        url = "profile_images/{username}/{file_name}".format(
            username=self.username,
            file_name=filename,
        )
        return url


class User(AbstractUser):

    profile_image = models.ImageField(
        upload_to=generate_filename
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
