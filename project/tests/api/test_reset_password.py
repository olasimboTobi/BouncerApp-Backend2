from rest_framework.test import APITestCase
from django.urls import reverse
from db.models import User


class TestSetUp(APITestCase):

    def setUp(self):
        self.user = User.objects.create(first_name='olawale',last_name='kareem', otp_code = 123456,
                        email='olawalekareemdev@gmail.com',password='password123',is_verified=True)
        self.reset_password = reverse('reset-password')
        

    def test_user_invalid_request(self):
        res = self.client.post(self.reset_password, format="json")
        self.assertEqual(res.status_code, 400)
        self.assertNotEqual(res.status_code, 200)

    def test_must_be_a_registered_user_to_reset(self):
        email = 'olawalekareemdev@gmail.com'
        registered_email = self.user.email
        self.assertEqual(email, registered_email)

    def test_user_reset_otp_code_not_compromised(self):
        sent_otp = 123456
        user_otp = self.user.otp_code
        self.assertEqual(sent_otp, user_otp)

    def test_user_reset_endpoint_has_correct_http_method(self):
        res = self.client.get(self.reset_password)
        self.assertEqual(res.status_code, 405)
        self.assertNotEqual(res.status_code, 200)


    def test_user_reset_not_a_redirection(self):
        res = self.client.post(self.reset_password,format="json")
        self.assertNotEqual(res.status_code, 301)
