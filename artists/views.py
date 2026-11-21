from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewArtistForm
from .models import Artist

def artist_list(request):
    artists = Artist.objects.all()
    
    return render(request, 'artists/artist_list.html', {'artists': artists})

def home_view(request):
    if request.method == 'POST':
        form = NewArtistForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thank you for your application! We will review your portfolio and be in touch soon."
            )
            return redirect('home')
    else:
        form = NewArtistForm()

    return render(request, 'home.html', {'form': form})