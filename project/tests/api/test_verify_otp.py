from django.urls import reverse
from django.test import TestCase
from db.models import User


class TestViews(TestCase):

    def setUp(self):
        User.objects.create(
            first_name='James',
            last_name='Adebayo',
            email='jamesadebayo@gmail.com',
            password='mypassword',
            otp_code='123456',
            is_verified=False,
        )
        self.code = User.objects.get(otp_code='123456')
        self.name = 'verify'        

    def test_otp_verification(self):
        otp = '123456'
        verify_otp = self.code.otp_code
        self.assertEqual(otp, verify_otp)

    def test_view_url_at_wrong_location(self):
        response = self.client.post('/api/auth/v1/verify/')
        self.assertEqual(response.status_code, 404)

    def test_view_url_at_desired_location(self):
        response = self.client.post('/api/v1/otp/verify/', {'otp_code': '123456', 'email': 'jamesadebayo@gmail.com'})
        self.assertEqual(response.status_code, 200)
        
    def test_view_url_accessible_by_name(self):
        check = self.name
        response = self.client.post(reverse(check))
        self.assertEqual(response.status_code, 400)

    def test_get_method(self):
        url = 'http://127.0.0.1:18000/api/v1/otp/verify/'
        response = self.client.post(url)
        self.assertEqual(response.status_code, 400)
