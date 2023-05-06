from django.test import TestCase
from db.models.cart_model import Cart
from db.models.user_model import User


# Create your tests here.
class CartModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = User.objects.create(
            first_name='John',
            last_name='Johnson',
            email='john.johnson@gmail.com',
            password='johnny007',
            otp_code='654321',
        )

        Cart.objects.create(
            user_id=user,
            products={'Apple': 'Iphone', 'Apple': 'MacBook', 'Apple': 'Ipad'},
            total_cost=799999.99,
        )

    def setUp(self):
        self.cart = Cart.objects.all().first()

    def test_products_label(self):
        field_label = self.cart._meta.get_field('products').verbose_name
        self.assertEqual(field_label, 'products')

    def test_total_cost_label(self):
        field_label = self.cart._meta.get_field('total_cost').verbose_name
        self.assertEqual(field_label, 'total cost')

    def test_total_cost_max_length(self):
        max_digits = self.cart._meta.get_field('total_cost').max_digits
        self.assertEqual(max_digits, 9)

    def test_total_cost_deciaml_places(self):
        decimal_places = self.cart._meta.get_field('total_cost').decimal_places
        self.assertEqual(decimal_places, 2)

    def test_coupon_label(self):
        field_label = self.cart._meta.get_field('coupon').verbose_name
        self.assertEqual(field_label, 'coupon')

    def test_coupon_value(self):
        field_label = self.cart._meta.get_field('coupon').default
        self.assertEqual(field_label, False)
