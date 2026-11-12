from django.contrib import admin
from django.contrib.messages import views
from django.urls import path, include
from django.views.generic import TemplateView  
from subscriptions.views import service_view, edit_profile, delete_account
from bookings.views import event_view, dashboard, book_service, edit_booking, delete_booking

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('artists/', include('artists.urls')),
    path('accounts/', include('allauth.urls')),
    path('services/', service_view, name='services'),
    path('events/', event_view, name='events'),
    path('accounts/dashboard/', dashboard, name='dashboard'),
    path('book/<int:service_id>/', book_service, name='book_service'),
    path('booking/edit/<int:booking_id>/', edit_booking, name='edit_booking'),
    path('booking/delete/<int:booking_id>/', delete_booking, name='delete_booking'),
    path("profile/edit/", edit_profile, name="edit_profile"),
    path("profile/delete/",delete_account, name="delete_account"),
]

