#created this file to define the URL patterns for the echo app
from django.urls import path
from .views import EchoView, EchoFormView, LoginPageView, RegisterView, RegisterSuccessView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('echo/', EchoView.as_view()),
    path('echo-form/', EchoFormView.as_view(), name='echo_form'),
    path('log-in/', LoginPageView.as_view(), name='login'),
    path('registration/', RegisterView.as_view(), name='register'),
    path('register-success/', RegisterSuccessView.as_view(), name='register_success')
]
