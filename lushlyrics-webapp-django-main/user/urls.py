from django.urls import path
from .views import vistor, signout, LoginView
from django.contrib.auth import views as auth_views


app_name = 'user'

urlpatterns = [
    path('visitor/', vistor, name='visitor'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', signout, name='logout')
]
