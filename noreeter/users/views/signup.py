from django.contrib.auth import authenticate, login, get_user_model
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import CreateView

from users.forms import UserRegistForm


class SignupView(CreateView):

    model = get_user_model()

    template_name = "users/signup.html"
    form_class = UserRegistForm

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        profile_image = request.FILES.get("profile_image")
        profile = request.POST.get("profile")

        user = get_user_model().objects.create_user(
            username=username,
            password=password,
            email=email,
            profile_image=profile_image,
            profile=profile,
        )

        # Automatically login user after signup
        user = authenticate(
            username=username,
            password=password,
        )
        login(request, user)

        return redirect(reverse("towns"))
