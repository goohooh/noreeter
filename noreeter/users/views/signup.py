from django.contrib.auth import authenticate, login, get_user_model
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import TemplateView


class SignupView(TemplateView):
    template_name = "users/signup.html"

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        profile = request.POST.get("profile")
        profile_image = request.FILES.get("profile_image")
        # from IPython import embed; embed()
        get_user_model().objects.create_user(
            username=username,
            password=password,
            email=email,
            profile=profile,
            profile_image=profile_image,
        )

        user = authenticate(
            username=username,
            password=password,
        )

        login(request, user)

        return redirect(reverse("home"))
