from django.contrib import admin
from .models import Service, Booking

# Registrera dina modeller så att de syns i adminpanelen
admin.site.register(Service)
admin.site.register(Booking)
