#created this file to define the URL patterns for the echo app
from django.urls import path
from .views import EchoView, echo_form

urlpatterns = [
    path('echo/', EchoView.as_view()),
    path('echo-form/', echo_form)
]
