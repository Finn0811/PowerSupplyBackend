from django.db import models


# Create your models here.


class PowerSupply(models.Model):
    name = models.CharField(null=True, blank=True, max_length=256)
    battery_capacity = models.FloatField(null=True, blank=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Stromversorgung'
        verbose_name_plural = 'Stromversorgungen'


class Measurement(models.Model):
    power_supply = models.ForeignKey(PowerSupply, related_name='measurements', on_delete=models.CASCADE)
    value = models.FloatField(null=True, blank=True, max_length=64)
    type = models.CharField(default="VOLTAGE", max_length=16)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.power_supply.name

    class Meta:
        verbose_name = 'Messung'
        verbose_name_plural = 'Messungen'
