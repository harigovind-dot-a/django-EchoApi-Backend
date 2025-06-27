from django.test import TestCase

# Create your tests here.
from .models import Message
from django.test import Client

class EchoApiTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = '/echo/'
    
    def test_post_message(self):
        data = {'message': 'Testing'}
        response = self.client.post(self.url, data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('echo', response.json())
        self.assertEqual(response.json()['echo'], 'Testing')

    def test_get_message(self):
        Message.objects.create(content='Test message')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('messages', response.json())
        self.assertEqual(response.json()['messages'][0]['content'], 'Test message')
