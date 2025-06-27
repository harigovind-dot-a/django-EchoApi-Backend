from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt # This decorator is used to exempt the view from CSRF verification.
from django.views.decorators.http import require_http_methods  # Importing the require_http_methods decorator.
import json
from .models import Message  # Importing the Message model.

@csrf_exempt # Exempting the view from CSRF protection for demonstrating.
@require_http_methods(["GET", "POST"])
def echo_view(request):
    if request.method == 'POST':
        # Parse the JSON data from the request body
        data = json.loads(request.body) # {'msg':'asd'}
        # Return the same data as a JSON response
        message = data.get('message')  # Extracting 'message' from the JSON data
        msg_save = Message.objects.create(content=message)  # Saving the message to the database
        return JsonResponse({'echo': msg_save.content, 'timestamp' : msg_save.created_at}, status=200)  # Returning the saved
    elif request.method == 'GET':
        # For GET requests, Retrieve all messages from the database
        msgs = Message.objects.all().order_by('created_at')  # Fetching all messages Ordering by creation time.
        message_list = [{'content': msg.content, 'created_at': msg.created_at} for msg in msgs]  # Creating a list of messages
        return JsonResponse({'messages': message_list}, status=200) # Returning the list of messages as a JSON response