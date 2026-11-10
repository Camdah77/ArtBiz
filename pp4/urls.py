from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView  
from subscriptions.views import service_view
# Hämta BÅDE event_view och dashboard från bookings.views här:
from bookings.views import event_view, dashboard 

urlpatterns = [
    path('admin/', admin.site.urls), # Städade upp admin-raden lite för enkelhetens skull
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('artists/', include('artists.urls')),
    path('accounts/', include('allauth.urls')),
    path('services/', service_view, name='services'),
    path('events/', event_view, name='events'),
    # Ändrade från views.dashboard till bara dashboard:
    path('accounts/dashboard/', dashboard, name='dashboard'),
]
