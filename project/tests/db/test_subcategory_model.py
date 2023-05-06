from django.test import TestCase
from db.models.subcategory_model import SubCategory
from db.models.category_model import Category


class TestSubCategoryModel(TestCase):

    def setUp(self):
        self.subcategory = SubCategory.objects.create(category =Category.objects.create(title="test run"), title="title")
    
    def test_subcategory_model(self):
        check = self.subcategory
        self.assertTrue(isinstance(check, SubCategory))

    def test_object_name_is_title(self):
        check = self.subcategory
        self.assertNotEqual(str(check), "category")

    def test_title_max_length(self):
        check = SubCategory.objects.get(title="title")
        max_length = check._meta.get_field("title").max_length
        self.assertEqual(max_length, 50)

    def test_title_label(self):
        check = SubCategory.objects.get(title="title")
        field_label = check._meta.get_field("title").verbose_name
        self.assertEqual(field_label, "title")

    def test_category_label(self):
        check = SubCategory.objects.get(title="title")
        field_label = check._meta.get_field("category").verbose_name
        self.assertEqual(field_label, "category")

    def test_id_label(self):
        check = SubCategory.objects.get(title="title")
        field_label = check._meta.get_field("id").verbose_name
        self.assertEqual(field_label, "id")
