from django.contrib.auth import get_user_model
from django.views.generic.detail import DetailView


class ProfileView(DetailView):
    model = get_user_model()
    template_name = "users/profile.html"
    slug_field = "username"
