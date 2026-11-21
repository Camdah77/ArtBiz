from django.shortcuts import render
from .models import Artist

def artist_list(request):
    artists = Artist.objects.all()
    
    return render(request, 'artists/artist_list.html', {'artists': artists})