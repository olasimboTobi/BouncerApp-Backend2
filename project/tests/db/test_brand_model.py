from django.test import TestCase
from db.models.brands_model import *


class BrandTestCase(TestCase):

    def setUp(self):
        Brand.objects.create(name="Apple")
        Brand.objects.create(name="Samsung")
        Brand.objects.create(name="Huawei")

    def test_name_field(self):
        apple = Brand.objects.get(name="Apple")
        samsung = Brand.objects.get(name="Samsung")
        huawei = Brand.objects.get(name="Huawei")
        self.assertEqual(apple.name, 'Apple')
        self.assertEqual(samsung.name, 'Samsung')
        self.assertEqual(huawei.name, 'Huawei')

    def test_field_label(self):
        apple = Brand.objects.get(name="Apple")
        samsung = Brand.objects.get(name="Samsung")
        huawei = Brand.objects.get(name="Huawei")
        field_label_apple = apple._meta.get_field('name').verbose_name
        field_label_samsung = samsung._meta.get_field('name').verbose_name
        field_label_huawei = huawei._meta.get_field('name').verbose_name
        self.assertEqual(field_label_apple, 'name')
        self.assertEqual(field_label_samsung, 'name')
        self.assertEqual(field_label_huawei, 'name')

    def test_data_id(self):
        apple = Brand.objects.get(name="Apple")
        samsung = Brand.objects.get(name="Samsung")
        huawei = Brand.objects.get(name="Huawei")
        self.assertNotIsInstance(apple.id, int)
        self.assertNotIsInstance(samsung.id, int)
        self.assertNotIsInstance(huawei.id, int)

    def test_unique_name(self):
        apple = Brand.objects.get(name="Apple")
        samsung = Brand.objects.get(name="Samsung")
        huawei = Brand.objects.get(name="Huawei")
        self.assertNotEqual(apple.name, samsung.name)
        self.assertNotEqual(samsung.name, huawei.name)
        self.assertNotEqual(apple.name, huawei.name)

    def test_name_field_instance(self):
        apple = Brand.objects.get(name="Apple")
        samsung = Brand.objects.get(name="Samsung")
        huawei = Brand.objects.get(name="Huawei")
        self.assertIsInstance(apple, object)
        self.assertIsInstance(samsung, object)
        self.assertIsInstance(huawei, object)
