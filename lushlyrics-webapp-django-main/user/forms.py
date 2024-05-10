from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username',
            'style': 'width: 100%; border-radius: 20px; padding: 6px;'
        }))

    password = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'style': 'width: 100%; border-radius: 20px; padding: 6px;'
        }))
