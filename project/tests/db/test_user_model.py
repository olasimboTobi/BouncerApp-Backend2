from django.test import TestCase
from db.models.user_model import User


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(
            first_name='James',
            last_name='Adebayo',
            email='jamesadebayo@gmail.com',
            password='mypassword',
            otp_code='123456',
            is_verified=False,
        )

    def test_first_name_label(self):
        user_uuid = User.objects.all().first().id
        user = User.objects.get(id=user_uuid)
        field_label = user._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_first_name_max_length(self):
        user_uuid = User.objects.all().first().id
        user = User.objects.get(id=user_uuid)
        max_length = user._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 250)

    def test_last_name_label(self):
        user_uuid = User.objects.all().first().id
        user = User.objects.get(id=user_uuid)
        field_label = user._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'last name')

    def test_last_name_max_length(self):
        user_uuid = User.objects.all().first().id
        user = User.objects.get(id=user_uuid)
        max_length = user._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 250)

    def test_otp_label(self):
        user_uuid = User.objects.all().first().id
        user = User.objects.get(id=user_uuid)
        field_label = user._meta.get_field('otp_code').verbose_name
        self.assertEqual(field_label, 'otp code')

    def test_otp_max_length(self):
        user_uuid = User.objects.all().first().id
        user = User.objects.get(id=user_uuid)
        max_length = user._meta.get_field('otp_code').max_length
        self.assertEqual(max_length, 6)

    def test_email_max_length(self):
        user_uuid = User.objects.all().first().id
        user = User.objects.get(id=user_uuid)
        max_length = user._meta.get_field('email').max_length
        self.assertEqual(max_length, 254)

    def test_password_max_length(self):
        user_uuid = User.objects.all().first().id
        user = User.objects.get(id=user_uuid)
        max_length = user._meta.get_field('password').max_length
        self.assertEqual(max_length, 255)

    def test_is_verified_label(self):
        user_uuid = User.objects.all().first().id
        user = User.objects.get(id=user_uuid)
        field_label = user._meta.get_field('is_verified').verbose_name
        self.assertEqual(field_label, 'is verified')

    def test_is_created_label(self):
        user_uuid = User.objects.all().first().id
        user = User.objects.get(id=user_uuid)
        field_label = user._meta.get_field('created_at').verbose_name
        self.assertEqual(field_label, 'created at')

    def test_is_updated_label(self):
        user_uuid = User.objects.all().first().id
        user = User.objects.get(id=user_uuid)
        field_label = user._meta.get_field('updated_at').verbose_name
        self.assertEqual(field_label, 'updated at')

    def test_object_name_is_first_name_comma_last_name(self):
        user_uuid = User.objects.all().first().id
        user = User.objects.get(id=user_uuid)
        expected_object_name = f'{user.first_name}, {user.last_name}'
        self.assertEqual(str(user), expected_object_name)
