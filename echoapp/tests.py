from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Message

class EchoApiTest(APITestCase):
    def setUp(self):
        self.url = '/echo/'

        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
    
    def test_post_message(self):
        data = {'message': 'Testing'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('content', response.json())
        self.assertEqual(response.json()['content'], 'Testing')

    def test_get_message(self):
        Message.objects.create(content='Test message')
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('all messages', response.json())
        self.assertEqual(response.json()['all messages'][0]['content'], 'Test message')
