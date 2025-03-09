from django.shortcuts import render


def show_home_app(request):
    return render(request, "HomeApp/home.html")