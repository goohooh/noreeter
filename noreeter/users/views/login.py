from django.contrib.auth import login, authenticate
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import TemplateView

from users.forms import LoginForm


class LoginView(TemplateView):
    template_name = "users/login.html"

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        next_page = request.POST.get("next") or reverse("home")

        user = authenticate(
            username=username,
            password=password,
        )

        if user:
            login(
                request,
                user,
            )

            return redirect(next_page)
        return redirect(reverse("login") + '?next={next_page_name}'.format(
                next_page_name=next_page,
            )
        )

    def get_context_data(self):
        context = super(LoginView, self).get_context_data()
        context["form"] = LoginForm()
        return context
