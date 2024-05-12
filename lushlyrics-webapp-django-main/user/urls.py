from django.urls import path
from .views import vistor, signout
from django.contrib.auth import views as auth_views
from .forms import SigninForm, ForgotPasswordForm

app_name = 'user'

urlpatterns = [
    path('visitor/', vistor, name='visitor'),
    path('login/', auth_views.LoginView.as_view(authentication_form=SigninForm), name='login'),
    path('logout/', signout, name='logout'),
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name="registration/forgot_password_form.html", form_class=ForgotPasswordForm), name='forgot-password'),
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password-change'),
]
