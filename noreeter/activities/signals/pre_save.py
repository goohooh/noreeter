from django.db.models.signals import pre_save
from django.dispatch import receiver

from activities.models import Activity


@receiver(pre_save, sender=Activity)
def pre_save_activity(sender, instance, *args, **kwargs):
    instance.town = instance.host.town
