from django.db import models

class Artist(models.Model):
    # Information om konstnären
    artist_name = models.CharField(max_length=100)
    image_profile = models.URLField(max_length=500, blank=True, verbose_name="Profile image (Cloudinary-länk)")
    image_art = models.URLField(max_length=500, blank=True, verbose_name="Environment image (Cloudinary-länk)")
    description = models.TextField(blank=True, verbose_name="Description")
    exhibitions = models.TextField(blank=True, verbose_name="Exhibitions")
        
    def __str__(self):
        return self.artist_name
