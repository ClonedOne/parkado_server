from service.models import Parking
from rest_framework import serializers


class ParkingSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parking
        fields = ('car_type', 'created', 'lastLat', 'lastLong', 'parked')
