from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm


class SigninForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username',
            'style': 'width: 100%; height: 1.5rem; border-radius: 5px; padding: 10px;'
        }))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'style': 'width: 100%; height: 1.5rem; border-radius: 5px; padding: 10px;'
        }))


class ForgotPasswordForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'style': 'width: 100%; height: 1.5rem; border-radius: 5px; padding: 10px;'
        }
    ))

