import uuid
from django.db import models
from db.models.user_model import User


# Create your models here.
class Cart(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.JSONField(encoder=None)
    total_cost = models.DecimalField(max_digits=9, decimal_places=2)
    coupon = models.BooleanField(default=False)

    def __str__(self):
        return self.products
