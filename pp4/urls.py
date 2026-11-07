from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView  # Lägg till denna import!

urlpatterns = [
    path('admin/', admin.site.split_view if hasattr(admin.site, 'split_view') else admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),  # Kopplar din wireframe till http://127.0.0.1:8000/
    path('artists/', include('artists.urls')),
]
