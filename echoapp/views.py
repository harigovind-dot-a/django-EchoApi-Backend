from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt # This decorator is used to exempt the view from CSRF verification.
import json
from .models import Message  # Importing the Message model.

@csrf_exempt # Exempting the view from CSRF protection for demonstrating.
def echo_view(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body)
            # Return the same data as a JSON response
            message = data.get('message', '')  # Extracting 'message' from the JSON data
            if not message:
                return JsonResponse({'error': 'Message is required'}, status=400)
            else:
                pass
            msg_save = Message.objects.create(content=message)  # Saving the message to the database
            return JsonResponse({'echo': msg_save.content, 'timestamp' : msg_save.created_at}, status=200)  # Returning the saved
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    elif request.method == 'GET':
        # For GET requests, Retrieve all messages from the database
        msg_retrieved = Message.objects.all().order_by('created_at')  # Fetching all messages Ordering by creation time.
        message_list = [{'content': msg.content, 'created_at': msg.created_at} for msg in msg_retrieved]  # Creating a list of messages
        return JsonResponse({'messages': message_list}, status=200) # Returning the list of messages as a JSON response
    else:
        return JsonResponse({'error': 'Only POST and GET Method allowed'}, status=405)
