# project/urls.py

from django.urls import path
from knox.views import custom_login_view, signup_view, loggedin_view, loggedout_view, logout_view, home_view
from django.contrib import admin
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('login/', custom_login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('loggedin/', loggedin_view, name='loggedin'),
    path('logoutting/', logout_view, name='logoutting'),
    path('loggedout/', loggedout_view, name='loggedout'),
    path('', home_view, name='home'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),
    path('reset/done/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'),
]
