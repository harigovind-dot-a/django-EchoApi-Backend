#created this file to define the URL patterns for the echo app
from django.urls import path, include
from .views import EchoStoreViewSet, EchoFormView, LoginPageView, RegisterView, RegisterSuccessView, LogoutView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'echo', EchoStoreViewSet, basename='echo')

urlpatterns = [
    path('log-in/', LoginPageView.as_view(), name='login'),
    path('', include(router.urls)),
    path('echo-form/', EchoFormView.as_view(), name='echo_form'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', RegisterView.as_view(), name='register'),
    path('register-success/', RegisterSuccessView.as_view(), name='register_success')
]
