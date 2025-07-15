from rest_framework import viewsets, permissions
from .serializers import MessageSerializer
from .models import Message, CustomUser
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
from rest_framework.decorators import action

@action(detail=False, methods=['post'], permission_classes=[permissions.IsAuthenticated])
class EchoStoreViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all().order_by('created_at')

class EchoFormView(TemplateView):
    template_name = 'echoapp/echo_form.html'

class LoginPageView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'echoapp/login.html')
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            temp_user = CustomUser(username=username, password=password, email="dummy@example.com")
            temp_user.full_clean()
        except ValidationError as e:
            messages.error(request, f"Validation error: {e}")
            return redirect('login')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('echo_form')
        else:
            messages.error(request, "Invalid username/password")
            return redirect('login')
            
class RegisterSuccessView(TemplateView):
    template_name = 'echoapp/registr_success.html'

class RegisterView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'echoapp/registration.html')
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')
        else:
            try: 
                user = CustomUser(username=username, email=email)
                user.set_password(password)
                user.full_clean()
                user.save()
                return redirect('register_success')
            except ValidationError as e:
                messages.error(request, f"Validation error: {e}")
                return redirect('register')
            except IntegrityError as e:
                if 'username' in str(e):
                    messages.error(request, "Username already exists.")
                elif 'email' in str(e):
                    messages.error(request, "Email already exists.")
                else:
                    messages.error(request, "Registration failed due to a database constraint.")
                return redirect('register')
