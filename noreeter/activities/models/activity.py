from django.conf import settings
from django.core.urlresolvers import reverse
from django.core.validators import MinValueValidator
from django.db import models

from interests.models import Interest
from towns.models import Town


class Activity(models.Model):
    host = models.ForeignKey(
        settings.AUTH_USER_MODEL,
    )

    title = models.CharField(
        max_length=30,
    )

    content = models.TextField()

    image = models.ImageField(
        upload_to='images/%y/%m/%d',
    )

    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )

    category_set = models.ManyToManyField(
        Interest,
    )

    due_datetime = models.DateTimeField()

    town = models.ForeignKey(
        Town,
    )

    participant_set = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="participate_set"
    )

    is_full = models.BooleanField(
        default=False,
    )

    max_num_of_participant = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)],
        default=1,
    )

    @property
    def num_of_participant(self):
        return self.participant_set.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "activity",
            kwargs={
                "pk": self.id,
            }
        )

    @property
    def korean_due_datetime(self):
        return '{month}월{day}일 {hour}시 {minute}분'.format(
            month=self.due_datetime.month,
            day=self.due_datetime.day,
            hour=self.due_datetime.hour,
            minute=self.due_datetime.minute,
        )
