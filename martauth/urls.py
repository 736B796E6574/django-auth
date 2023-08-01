# project/urls.py

from django.urls import path
from knox.views import custom_login_view, signup_view
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', custom_login_view, name='login'),
    path('signup/', signup_view, name='signup'),
]
