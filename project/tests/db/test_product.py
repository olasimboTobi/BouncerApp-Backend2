from django.test import TestCase
from django.utils import timezone
from db.models.product_model import *


class ProductModelTest(TestCase):

    def setUp(self):
        laptops = Category.objects.create(title='Laptops')
        apple = Brand.objects.create(name='Apple')
        microsoft = Brand.objects.create(name='Microsoft')
        self.MacAir = Product.objects.create(
            name='MacAir',
            image='https://unsplash.com/s/photos/iphone10',
            price=99.99,
            category=laptops,
            label='mac',
            brand=apple,
            quantity_in_stock=10,
            discounted_price=90.99,
            shipping_fee=10.00,
            description='A tool and luxury of now'
        )
        self.HpEnvy = Product.objects.create(
            name='HpEnvy',
            image='https://unsplash.com/s/photos/iphone10',
            price=60.99,
            category=laptops,
            label='windows',
            brand=microsoft,
            quantity_in_stock=10,
            discounted_price=50.99,
            shipping_fee=10.00,
            description='A versatile and affordable product'
        )

    def test_product_name(self):
        self.assertEqual(self.MacAir.name, 'MacAir')
        self.assertEqual(self.HpEnvy.name, 'HpEnvy')

    def test_product_category(self):
        self.assertEqual(self.MacAir.category.title, 'Laptops')
        self.assertEqual(self.HpEnvy.category.title, 'Laptops')

    def test_product_brand(self):
        self.assertEqual(self.MacAir.brand.name, 'Apple')
        self.assertEqual(self.HpEnvy.brand.name, 'Microsoft')

    def test_product_description(self):
        self.assertEqual(self.MacAir.description, 'A tool and luxury of now')
        self.assertEqual(self.HpEnvy.description,
                         'A versatile and affordable product')

    def test_product_model_field_brand(self):
        field_label_mac = self.MacAir._meta.get_field('brand').verbose_name
        field_label_windows = self.HpEnvy._meta.get_field('brand').verbose_name
        self.assertEqual(field_label_mac, 'brand')
        self.assertEqual(field_label_windows, 'brand')

    def test_product_model_field_category(self):
        field_label_mac = self.MacAir._meta.get_field('category').verbose_name
        field_label_windows = self.HpEnvy._meta.get_field(
            'category').verbose_name
        self.assertEqual(field_label_mac, 'category')
        self.assertEqual(field_label_windows, 'category')

    def test_product_arrival_time(self):
        time_now = timezone.now()
        product_time_mac = self.MacAir.created_at
        product_time_windows = self.HpEnvy.created_at
        self.assertNotEqual(product_time_mac, time_now)
        self.assertNotEqual(product_time_windows, time_now)
