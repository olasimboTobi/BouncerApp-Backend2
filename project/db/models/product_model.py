import uuid
from django.db import models
from .brands_model import Brand
from .category_model import Category


class Product(models.Model):

    LARGE = 'L'
    MEDIUM = 'M'
    SMALL = 'S'

    SIZE_CHOICES = [
        (LARGE, 'Large'),
        (MEDIUM, 'Medium'),
        (SMALL, 'Small'),
    ]

    WHITE = 'WH'
    BLUE = 'BL'
    RED = 'RE'
    BLACK = 'BK'
    BROWN = 'BR'

    COLOUR_CHOICES = [
        (WHITE, 'White'),
        (BLUE, 'Blue'),
        (RED, 'Red'),
        (BLACK, 'BK'),
        (BROWN, 'Brown'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)
    image = models.URLField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='category')
    label = models.CharField(max_length=100)
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, related_name='brand')
    quantity_in_stock = models.IntegerField()
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_fee = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(
        max_length=50, choices=SIZE_CHOICES, default=MEDIUM)
    description = models.TextField(max_length=50)
    colour = models.CharField(
        max_length=50, choices=COLOUR_CHOICES, default=BLACK)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ['-created_at']
