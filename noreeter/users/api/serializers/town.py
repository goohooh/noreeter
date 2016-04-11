from rest_framework import serializers

from towns.models import Town


class TownListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Town
        fields = '__all__'
