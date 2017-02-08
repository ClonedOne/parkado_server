from service.models import Parking
from rest_framework import serializers


class ParkingSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parking
        fields = ('carType', 'created', 'lastLat', 'lastLong', 'parked')
