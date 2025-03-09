from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def show_auth(request):
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")
        password_repeat = request.POST.get("password_repeat")
        if password == password_repeat:
            user = authenticate(request = request, username = name, password = password)
            if user != None:
                login(request = request, user = user)
                return redirect("home")
            else:
                messages.error(request = request, message = "Логін або пароль не вірні!😢")
                return redirect("auth")

    return render(request, "UserApp/auth.html")

def show_reg(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_repeat =  request.POST.get("password_repeat")
        if password == password_repeat:
            try:
                user = User.objects.create_user(username = name, email = email, password = password)
                Profile.objects.create(user = user)
                return redirect("auth")
            except IndexError:
                messages.error(request = request, message = "Такий користувач уже існує!")
                return redirect("reg")
        else:
            messages.error(request = request, message = "Паролі не співпадають")
            return redirect("reg")
                
    return render(request, "UserApp/reg.html")

def logout_user(request):
    logout(request = request)
    return redirect('auth')


