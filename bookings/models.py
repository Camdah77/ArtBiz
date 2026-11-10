from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    """Representerar de tjänster som går att boka/prenumerera på"""
    SERVICE_TYPES = [
        ('event', 'Event/Class'),
        ('consulting', 'Consulting'),
        ('subscription', 'Subscription'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES, default='event')
    image_url = models.URLField(max_length=1024, blank=True, null=True) 
    
    def __str__(self):
        return self.title


class Booking(models.Model):
    """Representerar en specifik kunds bokning av en tjänst"""
    STATUS_CHOICES = [
        ('pending', 'Väntar på godkännande'),
        ('confirmed', 'Bekräftad'),
        ('cancelled', 'Avbokad'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    service = models.ForeignKey(Service, on_delete=models.PROTECT, related_name='booked_services')
    booking_date = models.DateTimeField() 
    number_of_participants = models.PositiveIntegerField(default=5) 
    created_at = models.DateTimeField(auto_now_add=True) 
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True, null=True) 

    def __str__(self):
        return f"{self.user.username} - {self.service.title} ({self.booking_date.strftime('%Y-%m-%d')})"