from django.contrib.auth import authenticate, login, get_user_model
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView

from users.forms import UserRegistForm


class SignupView(CreateView):
    model = get_user_model()
    template_name = "users/signup.html"
    form_class = UserRegistForm
    success_url = "/town/set/"
