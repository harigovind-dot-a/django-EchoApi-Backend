#created this file to define the URL patterns for the echo app
from django.urls import path
from .views import EchoView, EchoFormView, LoginPageView, RegisterView, RegisterSuccessView

urlpatterns = [
    path('', LoginPageView.as_view(), name='login'),
    path('echo/', EchoView.as_view()),
    path('echo-form/', EchoFormView.as_view(), name='echo_form'),
    path('registration/', RegisterView.as_view(), name='register'),
    path('register-success/', RegisterSuccessView.as_view(), name='register_success')
]
