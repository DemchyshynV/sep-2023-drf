from rest_framework import serializers

from apps.auto_parks.models import AutoParkModel
from apps.cars.serializers import CarSerializer


class AutoParkSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)
    class Meta:
        model = AutoParkModel
        fields = ('id', 'name', 'cars')
        # depth = 1

