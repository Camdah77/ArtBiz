from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView  

urlpatterns = [
    path('admin/', admin.site.split_view if hasattr(admin.site, 'split_view') else admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('artists/', include('artists.urls')),
    path('accounts/', include('allauth.urls')),
]