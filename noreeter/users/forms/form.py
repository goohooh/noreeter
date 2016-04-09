from django import forms

from django.contrib.auth import get_user_model


class UserRegistForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'password',
            'email',
            'profile_image',
            'profile',
        ]
