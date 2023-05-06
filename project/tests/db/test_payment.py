from django.test import TestCase
from db.models.payment_model import Payment
from db.models.order_model import Order
from db.models.cart_model import Cart
from db. models.user_model import User


class PaymentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
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

        Payment.objects.create(status='already paid', order=order)

    def test_payment_max_length(self):
        payment_id = Payment.objects.all().first().id
        payment = Payment.objects.get(id=payment_id)
        max_length = Payment._meta.get_field('status').max_length
        self.assertEqual(max_length, 30)

    def test_model_str(self):
        payment_id = Payment.objects.all().first().id
        payment = Payment.objects.get(id=payment_id)
        self.assertEqual(str(payment), "already paid")

    def test_payment_label(self):
        payment_id = Payment.objects.all().first().id
        payment = Payment.objects.get(id=payment_id)
        field_label = payment._meta.get_field('phone_number').verbose_name
        self.assertEqual(field_label, 'phone number')
