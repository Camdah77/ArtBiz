from django import forms
from django.utils import timezone
from .models import Booking


class BookingForm(forms.ModelForm):
    """Form for customers to book or update a service"""
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

    def clean_booking_date(self):
        """Ensure the selected booking date is in the future"""
        booking_date = self.cleaned_data.get('booking_date')
        if booking_date and booking_date < timezone.now():
            raise forms.ValidationError(
                "You cannot book a date and time in the past. Please select a future date."
            )
        return booking_date
