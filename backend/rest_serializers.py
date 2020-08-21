from rest_framework import serializers

from backend.models import PowerSupply, Measurement


class RestPowerSupplySerializer(serializers.ModelSerializer):
    # measurements = RestMeasurementSerializer(many=True, read_only=True)

    class Meta:
        model = PowerSupply
        fields = ('id', 'name', 'battery_capacity')
        read_only_fields = ('id',)


# https://stackoverflow.com/questions/41394761/the-create-method-does-not-support-writable-nested-fields-by-default
class RestMeasurementSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super(RestMeasurementSerializer, self).to_representation(instance)
        representation['power_supply'] = RestPowerSupplySerializer(instance.power_supply, many=False).data
        return representation

    class Meta:
        model = Measurement
        fields = ('id', 'power_supply', 'value', 'type', 'timestamp')
        read_only_fields = ('id',)
