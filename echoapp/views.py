from rest_framework import viewsets, permissions
from rest_framework.authtoken.models import Token
from .serializers import MessageSerializer
from .models import Message
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .forms import CustomRegisterForm

class EchoStoreViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all().order_by('created_at')
    permission_classes = [permissions.IsAuthenticated]

class EchoFormView(TemplateView):
    template_name = 'echoapp/echo_form.html'

class LoginPageView(FormView):
    template_name = 'echoapp/login.html'
    form_class = AuthenticationForm
    success_url = '/echo-form/'

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)
            
class RegisterSuccessView(TemplateView):
    template_name = 'echoapp/registr_success.html'

class RegisterView(FormView):
    template_name = 'echoapp/registration.html'
    form_class = CustomRegisterForm
    success_url = '/register-success/'

    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)
