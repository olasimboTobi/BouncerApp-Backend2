from django.test import TestCase
from db.models.rating_model import Rating
from db.models.product_model import Product
from db.models.category_model import Category
from db.models.brands_model import Brand


class RatingsTest(TestCase):

    def setUp(self):
        laptops = Category.objects.create(title='Laptops')
        apple = Brand.objects.create(name='Apple')
        self.product = Product.objects.create(
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
        self.rate = Rating.objects.create(product= self.product, score=3.5, review='Good')
        self.rating = Rating.objects.get(review="Good")

    def test_rating_score_label(self):
        rating_value = self.rating._meta.get_field('score').verbose_name
        self.assertEqual(rating_value, 'score')

    def test_rating_review_label(self):
        review_label = self.rating._meta.get_field('review').verbose_name
        self.assertEqual(review_label, 'review')

    def test_str_method(self):
        self.assertEqual(str(self.rating), 'Good')

    def test_review_max_length(self):
        max_length = self.rating._meta.get_field('review').max_length
        self.assertEqual(max_length, 200)

    def test_rating_id_label(self):
        field_label = self.rating._meta.get_field('id').verbose_name
        self.assertEqual(field_label, 'id')
