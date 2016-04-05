from django.contrib.auth import login, authenticate
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = "users/login.html"

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            username=username,
            password=password,
        )

        if user:
            login(
                request,
                user,
            )

            return redirect(reverse("home"))
        return redirect(reverse("login"))
