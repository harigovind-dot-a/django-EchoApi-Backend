from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import MessageSerializer, EchoInputSerializer
from .models import Message
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import TemplateView, View
from django.contrib.auth import authenticate, login

class EchoView(APIView):
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return[IsAuthenticated()]
        return [AllowAny()]

    def post(self, request, *args, **kwargs):
        serializer = EchoInputSerializer(data=request.data)
        if serializer.is_valid():
            message = serializer.validated_data['message']
            msg_obj = Message.objects.create(content=message)
            return Response(MessageSerializer(msg_obj).data, status=status.HTTP_201_CREATED)

    def get(self, *args, **kwargs):
        msgs = Message.objects.all().order_by('created_at')
        serializer = MessageSerializer(msgs, many=True)
        return Response({'all messages': serializer.data}, status=status.HTTP_200_OK)

class EchoFormView(TemplateView):
    template_name = 'echoapp/echo_form.html'

class LoginPageView(TemplateView):

    def get(self, request, *args, **kwargs):
        return render(request, 'echoapp/login.html')
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            messages.error(request, "Username and password are required.")
            return redirect('login')
        elif len(username) < 8 or len(password) < 8:
            messages.error(request, "Username and password must be at least 8 characters.")
            return redirect('login')
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('echo_form')
            else:
                messages.error(request, "Invalid username or password.")
                return redirect('login')
            
class RegisterSuccessView(TemplateView):
    template_name = 'echoapp/registr_success.html'

class RegisterView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'echoapp/registration.html')
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if len(username) < 8 or len(password) < 8:
            messages.error(request, "Username and password must be at least 8 characters.")
            return redirect('register')        
        elif password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('register')
        else:
            User.objects.create_user(username=username, email=email, password=password).save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect('register_success')

class HomeView(TemplateView):
    template_name = 'echoapp/home.html'
