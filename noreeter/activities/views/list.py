from django.views.generic.list import ListView

from activities.models import Activity


class ActivityListView(ListView):
    model = Activity
    template_name = "activities/list.html"
    context_object_name = "activities"
