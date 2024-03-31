from react_framework import serializer

from shipment.models import Shipment


class ShipmentSerializer(serializer.ModelSerializer):
    class Meta:
        model = Shipment
        fields = "__all__"
