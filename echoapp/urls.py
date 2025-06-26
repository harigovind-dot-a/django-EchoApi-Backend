#created this file to define the URL patterns for the echo app
from django.urls import path
from .views import echo_view

urlpatterns = [
    path('echo/', echo_view),
]
