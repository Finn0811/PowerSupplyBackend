# Generated by Django 3.0.8 on 2020-07-10 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20200711_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='current',
            field=models.FloatField(blank=True, max_length=64, null=True),
        ),
    ]
