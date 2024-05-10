from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from .forms import LoginForm


def vistor(request):
    return render(request, 'vistor_page.html')

class LoginView(LoginView):
    form = LoginForm()

def signout(request):
    logout(request)
    return redirect('user:visitor')
