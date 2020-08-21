from django.contrib import admin

from backend.models import Measurement


class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['id', 'power_supply', 'value', 'type',  'timestamp']


admin.site.register(Measurement, MeasurementAdmin)
