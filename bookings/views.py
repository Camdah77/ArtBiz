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
    """Collects all bookable events/services and displays them"""
    services = Service.objects.all()
    context = {
        'services': services,
    }
    return render(request, 'event.html', context)


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

@login_required
def edit_booking(request, booking_id):
    """Allow logged-in users to edit their own booking"""
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your booking for "{booking.service.title}" has been updated.')
            return redirect('dashboard')
    else:
        form = BookingForm(instance=booking)

    context = {
        'form': form,
        'booking': booking,
        'service': booking.service,
    }
    return render(request, 'edit_booking.html', context)


@login_required
def delete_booking(request, booking_id):
    """Allow logged-in users to cancel/delete their own booking"""
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'POST':
        service_title = booking.service.title
        booking.delete()
        messages.success(request, f'Your booking for "{service_title}" has been cancelled.')
        return redirect('dashboard')

    context = {
        'booking': booking,
    }
    return render(request, 'delete_booking.html', context)
