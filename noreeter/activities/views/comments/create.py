from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from activities.models import Activity, Comment


class ActivityCommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = [
        'content',
    ]

    def form_valid(self, form):
        activity = Activity.objects.get(
           id=self.kwargs.get('pk')
        )

        form.instance.activity = activity
        form.instance.user = self.request.user

        return super(ActivityCommentCreateView, self).form_valid(form)

    def get_success_url(self):
        activity = Activity.objects.get(
            id=self.kwargs.get('pk')
        )
        return activity.get_absolute_url()
