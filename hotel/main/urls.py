"""hotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main-page'),
    path('gallery', views.gallery, name='gallery-page'),
    path('restaurant', views.restaurant, name='food-page'),
    path('contact', views.contact, name='contact-page'),
    path('room', views.room, name='room-page'),
    path('service', views.service, name='service-page'),
    path('en', views.en, name='en-page')
]
