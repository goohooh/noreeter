from django.views.generic import ListView

from activities.models import Activity


class HomeView(ListView):
    model = Activity
    template_name = "home.html"
    context_object_name = "activities"

    def get_queryset(self):
        queryset = super(HomeView, self).get_queryset()
        return queryset[:20]
