
from django.urls import re_path
from .api import login, register, profile, logout

urlpatterns = [
    re_path('login', login),
    re_path('register', register),
    re_path('profile', profile),
    re_path('logout', logout)
]