from django.http import HttpResponse
from rest_framework.views import APIView

from activities.models import Activity


class ParticipateAPIView(APIView):

    def post(self, request, *args, **kwargs):
        activity = Activity.objects.get(id=request.POST.get("activityID"))
        activity.participant_set.add(request.user)
        return HttpResponse(status=201)
