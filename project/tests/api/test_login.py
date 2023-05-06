from django.urls import include, path, reverse
from django.test import TestCase
from rest_framework.authtoken.models import Token
from rest_framework import status

class TestLogin(TestCase):
   
    def setUp(self):
        self.name = 'login'
    
    def test_password_encrypted(self):
        data = {
            "username" :"foluke",
             "password" : "password123"
            }
        response = self.client.post('login', data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
