from django.forms import ModelForm

from django.contrib.auth import get_user_model


class UserRegistForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'password',
            'email',
            'profile_image',
            'profile',
        ]
