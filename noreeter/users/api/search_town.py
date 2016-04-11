from rest_framework.generics import ListAPIView

from rest_framework import filters

from .serializers import TownListModelSerializer
from towns.models import Town


class TownListAPIView(ListAPIView):
    serializer_class = TownListModelSerializer

    def get_queryset(self):
        query = self.request.GET.get('search')
        return Town.objects.filter(town_name__contains=query)
