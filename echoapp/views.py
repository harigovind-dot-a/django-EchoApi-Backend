from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import MessageSerializer, EchoInputSerializer
from .models import Message
from django.shortcuts import render

class EchoView(APIView):
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

def echo_form(request):
    return render(request, 'echoapp/echo_form.html')
