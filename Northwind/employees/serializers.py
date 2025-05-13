from rest_framework import serializers
from .models import Employee, Territory, EmployeeTerritory

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class TerritorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Territory
        fields = "__all__"

class EmployeeTerritorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeTerritory
        fields = "__all__"