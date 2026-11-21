from django import forms
from .models import ArtistApplication


class NewArtistForm(forms.ModelForm):
    class Meta:
        model = ArtistApplication
        fields = ['your_name', 'contact_email', 'message']
        labels = {
            'your_name': 'Your name',
            'contact_email': 'Contact email',
            'message': 'Tell us about your art, your exhibitions and give us a link to your Social Media',
        }
        widgets = {
            'your_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your full name'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
