from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
# This code defines the URL patterns for the polls application in Django.
# It imports the necessary modules and the views from the current package.