from django import forms

from django.contrib.auth import get_user_model

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit


class UserRegistForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UserRegistForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.fields['username'].label = '이용자 아이디'
        self.fields['password'].label = '비밀번호'
        self.fields['email'].label = '이메일'
        self.fields['profile_image'].label = '프로필 이미지'
        self.fields['profile'].label = '자기 소개'
        self.helper.layout = Layout(
            'username',
            'password',
            'email',
            'profile_image',
            'profile',
        )


class UserTownSetForm(forms.ModelForm):
    search = forms.CharField()
    result = forms.MultipleChoiceField()

    class Meta:
        model = get_user_model()
        fields = [
            'search',
            'result',
        ]

    def __init__(self, *args, **kwargs):
        super(UserTownSetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
