#created this file to define the URL patterns for the echo app
from django.urls import path
from .views import EchoView

urlpatterns = [
    path('echo/', EchoView.as_view()),
]
