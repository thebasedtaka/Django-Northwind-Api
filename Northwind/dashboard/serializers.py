from rest_framework import serializers
from .models import Dashboard

class DashboardMetricsSerializer(serializers.Serializer):
    class Meta:
        model = Dashboard
        fields = '__all__'