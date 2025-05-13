from rest_framework import viewsets
from .models import Shipper
from .serializers import ShipperSerializer

class ShipperViewSet(viewsets.ModelViewSet):
    queryset = Shipper.objects.all()
    serializer_class = ShipperSerializer