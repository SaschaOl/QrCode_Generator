"""
URL configuration for QRCodeGen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from HomeApp.views import show_home_app
from ContactsApp.views import show_contacts
from SubscriptionApp.views import show_subsription_app
from .settings import MEDIA_ROOT, MEDIA_URL, DEBUG
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_home_app, name = 'home'),
    path('contacts/', show_contacts, name = 'contacts'),
    path('subscription/', show_subsription_app, name = 'subscription'),
    path('user/', include('UserApp.urls')),
    path('qrcode/', include('QRCodeApp.urls'))
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)