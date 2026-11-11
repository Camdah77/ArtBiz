from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """Form for customers to book a service"""
    class Meta:
        model = Booking
        fields = ['booking_date', 'number_of_participants', 'notes']
        widgets = {
            'booking_date': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'class': 'form-control',
                }
            ),
            'number_of_participants': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'min': 1,
                }
            ),
            'notes': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3,
                    'placeholder': 'Any special requests or questions?',
                }
            ),
        }
        labels = {
            'booking_date': 'Preferred Date & Time',
            'number_of_participants': 'Number of Participants',
            'notes': 'Additional Notes (Optional)',
        }
