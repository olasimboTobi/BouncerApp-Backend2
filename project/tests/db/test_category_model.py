from django.test import TestCase
from db.models.category_model import Category


class TestCategoryModel(TestCase):

    def setUp(self):
        self.category = Category.objects.create(title="title")

    def test_category_model(self):
        check = self.category
        self.assertTrue(isinstance(check, Category))
        
    def test_object_name_is_title(self):
        check = self.category
        self.assertEqual(str(check), "title")

    def test_created_at_label(self):
        category = Category.objects.get(title="title")
        field_label = category._meta.get_field("created_at").verbose_name
        self.assertEqual(field_label, "created at")
    
    def test_title_max_length(self):
        category = Category.objects.get(title="title")
        max_length = category._meta.get_field("title").max_length
        self.assertEqual(max_length, 50)
    
    def test_updated_at_label(self):
        category = Category.objects.get(title="title")
        field_label = category._meta.get_field("updated_at").verbose_name
        self.assertEqual(field_label, "updated at")
