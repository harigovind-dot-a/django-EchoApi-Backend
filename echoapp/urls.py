#created this file to define the URL patterns for the echo app
from django.urls import path
from .views import EchoView, echo_form, login_page, register_success, register, home

urlpatterns = [
    path('', home, name='home'),
    path('echo/', EchoView.as_view()),
    path('echo-form/', echo_form),
    path('log-in/', login_page),
    path('registration/', register, name='register'),
    path('register-success/', register_success, name='register_success')
]
