from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    # Kopplar bokningen till en specifik inloggad användare (företag)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    
    # Information om företaget och eventet
    company_name = models.CharField(max_length=100)
    event_date = models.DateTimeField()
    number_of_participants = models.IntegerField()
    special_requests = models.TextField(blank=True, null=True)
    
    # Automatiskt datum när bokningen skapades
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company_name} - {self.event_date.strftime('%Y-%m-%d')}"

# Create your models here.
