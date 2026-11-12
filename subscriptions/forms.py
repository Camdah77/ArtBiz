from allauth.account.forms import SignupForm
from django import forms
from .models import UserProfile


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(
        max_length=30, label="First Name", required=True
    )
    last_name = forms.CharField(
        max_length=30, label="Last Name", required=True
    )
    company_name = forms.CharField(
        max_length=100, label="Company Name", required=False
    )

    def save(self, request):
        user = super().save(request)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.save()

        UserProfile.objects.create(
            user=user, company_name=self.cleaned_data["company_name"]
        )
        return user
