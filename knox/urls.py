# project/urls.py

from django.urls import path
from knox.views import custom_login_view, signup_view, loggedin_view, loggedout_view, logout_view
from django.contrib import admin



urlpatterns = [
    path('login/', custom_login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('loggedin/', loggedin_view, name='loggedin'),
    path('logoutting/', logout_view, name='logoutting'),
    path('loggedout/', loggedout_view, name='loggedout'),
]
