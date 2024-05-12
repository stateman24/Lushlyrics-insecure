from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView


def vistor(request):
    return render(request, 'vistor_page.html')



def signout(request):
    logout(request)
    return redirect('user:visitor')
