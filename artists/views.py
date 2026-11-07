from django.shortcuts import render
from .models import Artist

def artist_list(request):
    # Hämtar ALLA konstnärer från databasen
    artists = Artist.objects.all()
    
    # Skickar med konstnärerna till HTML-mallen
    return render(request, 'artists/artist_list.html', {'artists': artists})
