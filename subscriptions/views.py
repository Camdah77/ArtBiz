from django.shortcuts import render
# Collect service-model from bookings app
from bookings.models import Service 

def service_view(request):
    """Collects all available services from the database and displays them"""
    services = Service.objects.all()
    
    context = {
        'services': services,
    }
    return render(request, 'services.html', context) 
