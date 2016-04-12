from django.http import HttpResponse
from rest_framework.views import APIView

from activities.models import Activity


class ParticipateAPIView(APIView):

    def post(self, request, *args, **kwargs):
        activity = Activity.objects.get(id=request.POST.get("activityID"))
        activity.participant_set.add(request.user)
        activity.num_of_participant + 1
        activity.save()
        return HttpResponse(status=201)
