from django.db import models


class Parking(models.Model):
    """
    Representing a Parking object. Has following properties:
    \car_type: int form 0 to 2 (citycar, sedan, suv)
    lastLat: double last known latitude
    lastLong: double last knwon longitude
    parked: bool true if currently parked

    """
    car_type = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    lastLat = models.FloatField(default=0)
    lastLong = models.FloatField(default=0)
    parked = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)
