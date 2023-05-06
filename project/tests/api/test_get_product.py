from db.models import Brand, Category, Product
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


# Create your tests here.
class ProductAPITest(APITestCase):

    def setUp(self):
        brand = Brand.objects.create(name='Apple')
        category = Category.objects.create(title='Laptops')
        self.product = Product.objects.create(
            name='Apple MacBook Pro',
            price=499.99,
            quantity_in_stock=101,
            discounted_price=0.99,
            shipping_fee=13.50,
            brand=brand,
            category=category
        )

    def test_get_all_product(self):
        url = reverse('product')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
