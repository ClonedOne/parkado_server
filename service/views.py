from service.serializers import ParkingSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from service.models import Parking
from rest_framework import status
from django.http import Http404


class ParkingViewSet(viewsets.ModelViewSet):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer


class ParkingList(APIView):
    """
      List all parkings, or create a new parking.
    """
    def get(self, request, format=None):
        parkings = Parking.objects.all()
        serializer = ParkingSerializer(parkings, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ParkingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ParkingDetail(APIView):
    """
    Retrieve, update or delete a parking instance.
    """
    def get_object(self, pk):
        try:
            return Parking.objects.get(pk=pk)
        except Parking.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        parking = self.get_object(pk)
        serializer = ParkingSerializer(parking)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        parking = self.get_object(pk)
        serializer = ParkingSerializer(parking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        parking = self.get_object(pk)
        parking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)