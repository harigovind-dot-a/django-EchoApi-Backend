from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from .serializers import MessageSerializer
from .models import Message
from .forms import RegisterForm
from django.http import JsonResponse
from django.views import View
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
import json

class EchoStoreViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all().order_by('created_at')
    # authentication_classes = [TokenAuthentication] # For template login to work.
    # permission_classes = [IsAuthenticatedOrReadOnly] # For template login to work
    permission_classes = [AllowAny] # For angular to GET and POST without auth. Remove this for django templates to work.

class EchoFormView(TemplateView):
    template_name = 'echoapp/echo_form.html'

@method_decorator(csrf_exempt, name='dispatch')
class LoginPageView(FormView):
    def get(self, request):
        return render(request, 'echoapp/login.html')

    def post(self, request):
        if request.headers.get("Content-Type") == "application/json":
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                Token.objects.filter(user=user).delete()
                token = Token.objects.create(user=user)
                return JsonResponse({'token': token.key})
            else:
                return JsonResponse({'error': 'Invalid credentials'}, status=400)
        else:
            return JsonResponse({'error': 'Invalid request'}, status=400)

class RegisterSuccessView(TemplateView):
    template_name = 'echoapp/registr_success.html'

class RegisterView(FormView):
    template_name = 'echoapp/registration.html'
    form_class = RegisterForm
    success_url = '/register-success/'

    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)
    
class LogoutView(View):
    def get(self, request):
        auth_header = request.headers.get("Authorization")
        if auth_header and auth_header.startswith("Token "):
            token_key = auth_header.split("Token ")[1]
            Token.objects.filter(key=token_key).delete()
            return redirect('/log-in/')
        else:
            pass
