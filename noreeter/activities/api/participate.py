import json

from rest_framework.views import APIView
from rest_framework.response import Response

from activities.models import Activity


class ParticipateAPIView(APIView):

    def get(self, request, *args, **kwargs):

        activity = Activity.objects.get(id=self.kwargs["pk"])

        if request.user in activity.participant_set.all():
            participant_list = [
                user.username
                for user
                in activity.participant_set.all()
            ]
            return Response({
                "participation_state": True,
                "participants": json.dumps(participant_list),
            })

        if activity.is_full:
            participant_list = [
                user.username
                for user
                in activity.participant_set.all()
            ]
            return Response({
                "participation_state": False,
                "is_full": True,
                "participants": json.dumps(participant_list),
            })

        participant_list = [
            user.username
            for user
            in activity.participant_set.all()
        ]
        return Response({
            "participation_state": False,
            "is_full": False,
            "participants": json.dumps(participant_list),
        })

    def post(self, request, *args, **kwargs):
        activity = Activity.objects.get(id=request.POST.get("activityID"))
        if activity.is_full:
            participant_list = [
                user.username
                for user
                in activity.participant_set.all()
            ]
            return Response(
                data={
                    "participants": json.dumps(participant_list),
                },
                status=412,
            )
        activity.participant_set.add(request.user)
        activity.num_of_participant + 1

        if activity.max_num_of_participant == activity.num_of_participant:
            activity.is_full = True
        activity.save()

        participant_list = [
            user.username
            for user
            in activity.participant_set.all()
        ]
        return Response(
            data={
                "participants": json.dumps(participant_list),
            },
            status=201
        )

    def delete(self, request, *args, **kwargs):
        activity = Activity.objects.get(id=self.kwargs["pk"])
        user = request.user
        activity.participant_set.remove(user)
        if activity.is_full:
            activity.is_full = False
        activity.save()

        participant_list = [
            user.username
            for user
            in activity.participant_set.all()
        ]
        return Response(
            data={
                "participants": json.dumps(participant_list),
            },
            status=201,
        )
