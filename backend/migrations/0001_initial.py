# Generated by Django 3.0.8 on 2020-07-10 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PowerSupply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('battery_capacity', models.FloatField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Stromversorgung',
                'verbose_name_plural': 'Stromversorgungen',
            },
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current', models.FloatField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('power_supply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='backend.PowerSupply')),
            ],
            options={
                'verbose_name': 'Messung',
                'verbose_name_plural': 'Messungen',
            },
        ),
    ]
