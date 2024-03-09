
from django.urls import re_path
from .api import login, register, profile

urlpatterns = [
    re_path('login', login),
    re_path('register', register),
    re_path('profile', profile)
]