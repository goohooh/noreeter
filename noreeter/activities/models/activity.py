from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models

from interests.models import Interest


class Activity(models.Model):
    host = models.ForeignKey(
        settings.AUTH_USER_MODEL,
    )

    title = models.CharField(
        max_length=30,
    )

    content = models.TextField()

    image = models.ImageField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )

    category_set = models.ManyToManyField(
        Interest,
        related_name="activity_set",
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "activity",
            kwargs={
                "pk": self.id,
            }
        )
