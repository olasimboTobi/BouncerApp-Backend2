from django.test import TestCase
from db.models.cart_model import Cart
from db.models.order_model import Order
from db. models.user_model import User


# Create your tests here.
class OrderModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = User.objects.create(
            first_name='Ayo',
            last_name='Ayooluwa',
            email='ayo.ayooluwa@gmail.com',
            password='ayooluwa757',
            otp_code='563412',
        )
        cart = Cart.objects.create(
            user_id=user,
            products={'Apple': 'Iphone', 'Apple': 'AirPods', 'Apple': 'Ipad'},
            total_cost=799999.99,
        )
        order = Order.objects.create(
            cart_id=cart,
            delivery_address='7 Asajon Way, Eti-Osa 234001, Sangotedo',
            delivery_status='Delivery in Progress'
        )

    def setUp(self):
        self.order = Order.objects.all().first()

    def test_delivery_address_label(self):
        field_label = self.order._meta.get_field(
            'delivery_address').verbose_name
        self.assertEqual(field_label, 'delivery address')

    def test_delivery_status_label(self):
        field_label = self.order._meta.get_field(
            'delivery_status').verbose_name
        self.assertEqual(field_label, 'delivery status')

    def test_delivery_status_max_length(self):
        max_length = self.order._meta.get_field('delivery_status').max_length
        self.assertEqual(max_length, 20)

    def test_delivery_status_value(self):
        expected_object_value = self.order.delivery_status
        self.assertEqual(expected_object_value, 'Delivery in Progress')
