from django.contrib import admin

from backend.models import PowerSupply


class PowerSupplyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'battery_capacity']


admin.site.register(PowerSupply, PowerSupplyAdmin)
