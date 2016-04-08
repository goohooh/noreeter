from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView


class ProfileView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = "users/profile.html"
    slug_field = "username"
