from django import urls
from django.urls import path
from . views import endpoint

urlpatterns = [
    path('',endpoint,name='home'),
]