from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'date_of_birth', 'phone_number', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    search_fields = ('email', 'full_name', 'phone_number')

# Register your CustomUser model with the custom admin class
admin.site.register(CustomUser, CustomUserAdmin)