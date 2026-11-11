from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking, Service
from .forms import BookingForm


@login_required
def dashboard(request):
    """Show user's bookings"""
    user_bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')
    
    context = {
        'bookings': user_bookings,
    }
    return render(request, 'account/dashboard.html', context)


def event_view(request):
    return render(request, 'event.html')


@login_required
def book_service(request, service_id):
    """Allow logged-in users to book a specific service"""
    service = get_object_or_404(Service, id=service_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.service = service
            booking.save()
            messages.success(request, f'Thank you! Your booking request for "{service.title}" has been received.')
            return redirect('dashboard')
    else:
        form = BookingForm()

    context = {
        'form': form,
        'service': service,
    }
    return render(request, 'book_service.html', context)
