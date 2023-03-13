from .views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('Contact', contact, name='Contact'),
    path('Elements', elements, name='Elements'),
    path('Portfolio', portfolio, name='Portfolio'),
    path('Services', services, name='Services'),
    path('Price', price, name='Price'),
    path('About', about, name='About'),
]
