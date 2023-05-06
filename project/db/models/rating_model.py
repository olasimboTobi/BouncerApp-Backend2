from django.db import models
import uuid
from .product_model import Product
 
    
class Rating(models.Model):   
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    score = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.TextField(max_length=200, null=True)
   
    def __str__(self):
       return self.review
