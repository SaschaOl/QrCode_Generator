from django.shortcuts import render
from UserApp.models import Profile
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def show_subsription_app(request: HttpRequest):
    profile = Profile.objects.get(user = request.user)
    if request.method == "POST":
        subscription = request.POST.get("sub")
        profile.subscription = subscription
        profile.save()
    return render(request, "SubscriptionApp/subscription.html", context={"sub": profile.subscription}) 
