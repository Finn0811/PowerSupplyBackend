# Generated by Django 3.0.8 on 2020-07-10 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='current',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
