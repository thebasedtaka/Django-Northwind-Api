from rest_framework import serializers
from .models import Shipper

class ShipperSerializer(serializers.ModelSerializer):
    model = Shipper
    fields = "__all__"
