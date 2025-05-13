from rest_framework import viewsets
from .models import Supplier
from .serializer import SupplierSerializers

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializers
