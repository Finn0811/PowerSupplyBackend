"""PowerSupplyBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from backend.views import rest_powersupplies, rest_measurements, rest_send_mqtt_message

urlpatterns = [
    path('admin/', admin.site.urls),

    path('rest/power_supplies', rest_powersupplies),
    path('rest/measurements', rest_measurements),

    path('rest/mqtt/send', rest_send_mqtt_message),
]
