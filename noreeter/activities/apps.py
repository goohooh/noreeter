from django.apps import AppConfig


class ActivitiesAppConfig(AppConfig):
    name = "activities"

    def ready(self):
        from activities.signals.pre_save import pre_save_activity
