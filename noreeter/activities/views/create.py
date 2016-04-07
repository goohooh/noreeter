from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import CreateView, FormView

from activities.forms import ActivityRegistForm
from activities.models import Activity


class ActivityCreateView(CreateView):
    model = Activity

    form_class = ActivityRegistForm
    template_name = "activities/create.html"

    def form_valid(self, form):
        form.instance.host = self.request.user
#        from IPython import embed; embed()
        return super(ActivityCreateView, self).form_valid(form)
