from django.db import models

class Artist(models.Model):
    artist_name = models.CharField(max_length=100)
    image_profile = models.URLField(max_length=500, blank=True, verbose_name="Profile image (Cloudinary-länk)")
    image_art = models.URLField(max_length=500, blank=True, verbose_name="Environment image (Cloudinary-länk)")
    description = models.TextField(blank=True, verbose_name="Description")
    exhibitions = models.TextField(blank=True, verbose_name="Exhibitions")
        
    def __str__(self):
        return self.artist_name

class ArtistApplication(models.Model):
    your_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Application from {self.your_name} ({self.contact_email})"
