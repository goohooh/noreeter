from django.views.generic import CreateView

from activities.models import Activity


class ActivityCreateView(CreateView):
    model = Activity

    fields = [
        "title",
        "content",
        "image",
    ]

    template_name = "activities/create.html"

    def form_valid(self, form):
        form.instance.host = self.request.user
        return super(ActivityCreateView, self).form_valid(form)
