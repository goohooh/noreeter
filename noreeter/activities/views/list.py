from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

from activities.models import Activity


class ActivityListView(LoginRequiredMixin, ListView):
    model = Activity
    template_name = "activities/list.html"
    context_object_name = "activities"
    ordering = '-updated_at'

    def get_queryset(self):
        user = self.request.user
        query = Activity.objects.filter(town=user.town)
        return query
