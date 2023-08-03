# project/urls.py

from django.urls import path, include
from knox.views import custom_login_view, signup_view
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('knox.urls')),
]



