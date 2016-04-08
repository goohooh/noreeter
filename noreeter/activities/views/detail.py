from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView

from activities.models import Activity


class ActivityDetailView(LoginRequiredMixin, DetailView):
    model = Activity
    template_name = "activities/detail.html"
