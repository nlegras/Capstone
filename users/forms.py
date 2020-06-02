from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Username", min_length=4, max_length=150, help_text = 'Register with your pawprint username')

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']