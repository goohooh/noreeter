from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from users.forms import UserTownSetForm
from towns.models import Town


class TownSetView(LoginRequiredMixin, TemplateView):
    template_name = "users/town_set.html"

    def post(self, request):
        selected_town = request.POST.get("result")
        user = self.request.user

        town = Town.objects.get(full_address=selected_town)

        user.town = town

        user.save()
        return redirect(
            reverse("home")
        )

    def get_context_data(self):
        context = super(TownSetView, self).get_context_data()
        context["form"] = UserTownSetForm()
        return context
