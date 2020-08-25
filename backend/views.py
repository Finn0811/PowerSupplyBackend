import json

from django.views.decorators.csrf import csrf_exempt
import paho.mqtt.client as mqtt
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from PowerSupplyBackend.settings import MQTT_IP
from backend.models import PowerSupply, Measurement
from backend.rest_serializers import RestPowerSupplySerializer, RestMeasurementSerializer


def get_int_or_default(param, default_value):
    def wrapper(view_func):
        def wrapped(request, *args, **kwargs):
            value = default_value

            try:
                value = int(request.GET.get(param, ''))
            except Exception:
                pass

            kwargs[param] = value
            return view_func(request, *args, **kwargs)

        return wrapped

    return wrapper


@csrf_exempt
@get_int_or_default("limit", None)
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def rest_powersupplies(req, *args, **kwargs):
    if req.method == 'GET':
        limit = kwargs['limit']

        power_supplies = PowerSupply.objects.all()[:limit]
        serializer = RestPowerSupplySerializer(power_supplies, many=True)
        return Response(serializer.data)

    return Response({"error": "Method not implemented."})


@csrf_exempt
@get_int_or_default("limit", None)
@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def rest_measurements(req, *args, **kwargs):
    if req.method == 'GET':
        limit = kwargs['limit']

        measurements = Measurement.objects.all().order_by('-timestamp')[:limit]
        serializer = RestMeasurementSerializer(measurements, many=True)
        return Response(serializer.data)

    if req.method == 'POST':
        serializer = RestMeasurementSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)

    return Response({"error": "Method not implemented."})


@csrf_exempt
@get_int_or_default("limit", None)
@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def rest_send_mqtt_message(req, *args, **kwargs):
    if req.method == 'POST':
        if 'power_supplies' in req.data and 'type' in req.data:
            client = mqtt.Client()
            client.connect(MQTT_IP)
            for power_supply_id in req.data['power_supplies']:
                client.publish("powersupply/trigger/", json.dumps({
                    'id': power_supply_id,
                    'trigger': req.data['type']
                }))
            client.disconnect()

        return Response({'success': 'Sent MQTT Message'}, status=200)

    return Response({"error": "Method not implemented."})
