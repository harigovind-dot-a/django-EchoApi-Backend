from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt # This decorator is used to exempt the view from CSRF verification.
import json

@csrf_exempt # Exempting the view from CSRF protection for demonstrating.
def echo_view(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body)
            # Return the same data as a JSON response
            return JsonResponse(data, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    elif request.method == 'GET':
        # For GET requests, return a simple message
        return JsonResponse({'message': 'Send a POST request with JSON data to echo it back.'}, status=200)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
