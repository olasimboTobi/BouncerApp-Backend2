from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


# Create your tests here.
class RegisterAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_api_can_create_user(self):
        valid_user_data = {
            'first_name': 'Tolani',
            'last_name': 'Akinola',
            'email': 'augustine.jibunoh@decagon.dev',
            'password': 'wiTTy007waTT'
        }
        self.response = self.client.post(
            reverse('register'),
            valid_user_data,
            format='json'
        )
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_firstname_field_may_not_be_blank(self):
        invalid_user_data = {
            'first_name': '',
            'last_name': 'Akinola',
            'email': 'augustine.jibunoh@decagon.dev',
            'password': 'wiTTy007waTT'
        }
        self.response = self.client.post(
            reverse('register'),
            invalid_user_data,
            format='json'
        )
        self.assertEqual(self.response.status_code,
                         status.HTTP_400_BAD_REQUEST)

    def test_api_lastname_field_may_not_be_blank(self):
        invalid_user_data = {
            'first_name': 'Tolani',
            'last_name': '',
            'email': 'augustine.jibunoh@decagon.dev',
            'password': 'wiTTy007waTT'
        }
        self.response = self.client.post(
            reverse('register'),
            invalid_user_data,
            format='json'
        )
        self.assertEqual(self.response.status_code,
                         status.HTTP_400_BAD_REQUEST)

    def test_api_email_field_may_not_be_blank(self):
        invalid_user_data = {
            'first_name': 'Tolani',
            'last_name': 'Akinola',
            'email': '',
            'password': 'wiTTy007waTT'
        }
        self.response = self.client.post(
            reverse('register'),
            invalid_user_data,
            format='json'
        )
        self.assertEqual(self.response.status_code,
                         status.HTTP_400_BAD_REQUEST)

    def test_api_password_field_may_not_be_blank(self):
        invalid_user_data = {
            'first_name': 'Tolani',
            'last_name': 'Akinola',
            'email': 'augustine.jibunoh@decagon.dev',
            'password': ''
        }
        self.response = self.client.post(
            reverse('register'),
            invalid_user_data,
            format='json'
        )
        self.assertEqual(self.response.status_code,
                         status.HTTP_400_BAD_REQUEST)
