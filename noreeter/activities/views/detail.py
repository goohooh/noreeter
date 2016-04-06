from django.views.generic.detail import DetailView

from activities.models import Activity


class ActivityDetailView(DetailView):
    model = Activity
    template_name = "activities/detail.html"
