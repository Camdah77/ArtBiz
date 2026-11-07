from django.contrib import admin
from django.urls import path, include  # Lägg till ', include' här

urlpatterns = [
    path('admin/', admin.site.split_view if hasattr(admin.site, 'split_view') else admin.site.urls), # Standard admin
    path('artists/', include('artists.urls')),  # Lägg till denna rad!
]
