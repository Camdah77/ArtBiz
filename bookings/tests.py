from datetime import timedelta
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Service, Booking
from .forms import BookingForm


class BookingAppTests(TestCase):
    """Automated tests for models, forms, views, and access control"""

    def setUp(self):
        """Create a test user, a second user, and a sample service"""
        self.user = User.objects.create_user(
            username='testclient',
            email='client@artbiz.com',
            password='StrongPassword123!'
        )
        self.other_user = User.objects.create_user(
            username='otherclient',
            email='other@artbiz.com',
            password='StrongPassword123!'
        )
        self.service = Service.objects.create(
            title='Corporate Painting Workshop',
            description='A creative team-building session.',
            service_type='event',
            price=250.00
        )
        self.future_date = timezone.now() + timedelta(days=5)
        self.booking = Booking.objects.create(
            user=self.user,
            service=self.service,
            booking_date=self.future_date,
            number_of_participants=8,
            notes='Window seats preferred'
        )

    def test_service_and_booking_str_methods(self):
        """Test string representations of Service and Booking models"""
        self.assertEqual(str(self.service), 'Corporate Painting Workshop')
        self.assertIn('testclient', str(self.booking))
        self.assertIn('Corporate Painting Workshop', str(self.booking))

    def test_booking_form_valid_future_date(self):
        """Test that BookingForm accepts a valid future date"""
        form = BookingForm(data={
            'booking_date': (timezone.now() + timedelta(days=3)).strftime('%Y-%m-%dT%H:%M'),
            'number_of_participants': 4,
            'notes': 'Looking forward to it!'
        })
        self.assertTrue(form.is_valid())

    def test_booking_form_rejects_past_date(self):
        """Test defensive validation rejecting dates in the past"""
        past_date = (timezone.now() - timedelta(days=2)).strftime('%Y-%m-%dT%H:%M')
        form = BookingForm(data={
            'booking_date': past_date,
            'number_of_participants': 2,
            'notes': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('booking_date', form.errors)

    def test_events_page_loads_successfully(self):
        """Test that public events page returns HTTP 200 and lists services"""
        response = self.client.get(reverse('events'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Corporate Painting Workshop')

    def test_dashboard_requires_login(self):
        """Test that unauthenticated users are redirected from dashboard"""
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)

    def test_authenticated_user_can_view_dashboard(self):
        """Test that logged-in user can view their own bookings on dashboard"""
        self.client.login(username='testclient', password='StrongPassword123!')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Corporate Painting Workshop')

    def test_user_cannot_edit_another_users_booking(self):
        """Test defensive access control preventing unauthorized edits"""
        self.client.login(username='otherclient', password='StrongPassword123!')
        response = self.client.get(reverse('edit_booking', args=[self.booking.id]))
        self.assertEqual(response.status_code, 404)

    def test_authenticated_user_can_delete_own_booking(self):
        """Test that a user can cancel/delete their own booking"""
        self.client.login(username='testclient', password='StrongPassword123!')
        response = self.client.post(reverse('delete_booking', args=[self.booking.id]))
        self.assertRedirects(response, reverse('dashboard'))
        self.assertFalse(Booking.objects.filter(id=self.booking.id).exists())
