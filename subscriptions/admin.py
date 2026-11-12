from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import UserProfile


# UserProfile 
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = "Company Information"


# Extend the default UserAdmin to include UserProfile
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)
    # Styr vilka kolumner som syns i den stora listan över användare
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "get_company_name",
        "is_staff",
    )
# Get the company name from the related UserProfile model
    def get_company_name(self, instance):
        # hasattr skyddar mot krasch om en gammal användare (t.ex. superuser) saknar UserProfile
        if hasattr(instance, "userprofile") and instance.userprofile.company_name:
            return instance.userprofile.company_name
        return "-"

    get_company_name.short_description = "Företag"  # Kolumnrubrik i admin
    
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = "Företagsinformation"


class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)
    # Styr vilka kolumner som syns i den stora listan över användare
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "get_company_name",
        "is_staff",
    )

    # Metod som hämtar företagsnamnet från UserProfile
    def get_company_name(self, instance):
        # hasattr skyddar mot krasch om en gammal användare (t.ex. superuser) saknar UserProfile
        if hasattr(instance, "userprofile") and instance.userprofile.company_name:
            return instance.userprofile.company_name
        return "-"

    get_company_name.short_description = "Företag"  # Kolumnrubrik i admin


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

