from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator 
import json
from .models import Message
from django.views import View

@method_decorator(csrf_exempt, name='dispatch')
class EchoView(View):
    def post(self, request):      
        data = json.loads(request.body) 
        message = data.get('message')
        msg_save = Message.objects.create(content=message)
        return JsonResponse({'echo': msg_save.content, 'timestamp' : msg_save.created_at}, status=200)
    def get(self, request):
        msgs = Message.objects.all().order_by('created_at')
        message_list = [{'content': msg.content, 'created_at': msg.created_at} for msg in msgs]
        return JsonResponse({'messages': message_list}, status=200)