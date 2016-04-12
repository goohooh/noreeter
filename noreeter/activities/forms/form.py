from django.forms import ModelForm

from activities.models import Activity


class ActivityRegistForm(ModelForm):
    class Meta:
        model = Activity
        exclude = [
            'host',
            'town',
            'participant_set',
            'is_full',
        ]
