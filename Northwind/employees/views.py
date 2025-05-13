from rest_framework import viewsets
from .models import Employee, Territory , EmployeeTerritory 
from .serializers import EmployeeSerializer, TerritorySerializer, EmployeeTerritorySerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class TerritoryViewSet(viewsets.ModelViewSet):
    queryset = Territory.objects.all()
    serializer_class = TerritorySerializer

class EmployeeTerritoryViewSet(viewsets.ModelViewSet):
    queryset = EmployeeTerritory.objects.all()
    serializer_class = EmployeeTerritorySerializer