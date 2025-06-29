from django.contrib import admin
from django.urls import path, include
from .views import home, contact_view

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact_view, name='contact'),
]
