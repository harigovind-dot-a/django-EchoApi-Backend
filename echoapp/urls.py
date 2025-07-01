#created this file to define the URL patterns for the echo app
from django.urls import path
from .views import EchoView, echo_form, login_page

urlpatterns = [
    path('echo/', EchoView.as_view()),
    path('echo-form/', echo_form),
    path('log-in/', login_page)
]
