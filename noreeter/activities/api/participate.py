import json

from django.http import HttpResponse

from rest_framework.views import APIView

from activities.models import Activity


class ParticipateAPIView(APIView):

    def get(self, request, *args, **kwargs):
        activity = Activity.objects.get(id=self.kwargs["pk"])

        if request.user in activity.participant_set.all():
            return HttpResponse(
                json.dumps({
                    "participation_state": True,
                }),
                content_type="application/json"
            )
        if activity.is_full:
            return HttpResponse(
                json.dumps({
                    "participation_state": False,
                    "is_full": True,
                }),
                content_type="application/json"
            )
        return HttpResponse(
            json.dumps({
                "participation_state": False,
                "is_full": False,
            }),
            content_type="application/json"
        )

    def post(self, request, *args, **kwargs):
        activity = Activity.objects.get(id=request.POST.get("activityID"))
        if activity.is_full:
            return HttpResponse(status=412)
        activity.participant_set.add(request.user)
        activity.num_of_participant + 1
        if activity.max_num_of_participant == activity.num_of_participant:
            activity.is_full = True
        activity.save()
        return HttpResponse(status=201)
