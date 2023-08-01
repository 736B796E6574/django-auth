# your_app/forms.py

from django import forms
from .models import CustomUser

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email', 'full_name', 'date_of_birth', 'phone_number', 'avatar', 'twitter', 'facebook', 'instagram', 'password')
