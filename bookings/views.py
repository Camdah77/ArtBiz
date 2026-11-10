from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Booking

@login_required
def dashboard(request):
    """Visar 'Min sida' för den inloggade användaren med deras bokningar"""
    # Ändrat från order_index_by till order_by
    user_bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')
    
    context = {
        'bookings': user_bookings,
    }
    return render(request, 'account/dashboard.html', context)

def event_view(request):
    return render(request, 'event.html')
