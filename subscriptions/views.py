from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import UserProfile

def service_view(request):
    """Displays an overview of what ArtBiz offers"""
    return render(request, 'services.html')
    
@login_required
def edit_profile(request):
    # get_or_create skyddar mot krasch om en gammal användare (t.ex. admin) saknar UserProfile
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Din profil har uppdaterats!")
            return redirect("dashboard")  # Kontrollera att ditt url-namn för dashboard stämmer
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=profile)

    context = {
        "u_form": u_form,
        "p_form": p_form,
    }
    return render(request, "subscriptions/edit_profile.html", context)


@login_required
def delete_account(request):
    if request.method == "POST":
        user = request.user
        logout(request)  # Logga ut användaren först
        user.delete()  # Raderar både User och kopplad UserProfile (tack vare on_delete=CASCADE)
        messages.success(request, "Ditt konto och all tillhörande data har raderats.")
        return redirect("home")  # Byt till namnet på din startsida (t.ex. 'home' eller 'index')

    return render(request, "subscriptions/delete_account.html")
