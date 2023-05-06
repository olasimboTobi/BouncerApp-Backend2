import uuid
from django.db import models
from db.models.cart_model import Cart


# Create your models here.
class Order(models.Model):
    PROCESSING_STOCK = 'Processing Stock'
    DELIVERY_IN_PROGRESS = 'Delivery in Progress'
    DELIVERED = 'Delivered'
    NOT_DELIVERED = 'Not Delivered'
    RETURNED = 'Returned'
    DELIVERY_STATUSES = [
        (PROCESSING_STOCK, 'Processing Stock'),
        (DELIVERY_IN_PROGRESS, 'Delivery in Progress'),
        (DELIVERED, 'Delivered'),
        (NOT_DELIVERED, 'Not Delivered'),
        (RETURNED, 'Returned'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    delivery_address = models.TextField()
    delivery_status = models.CharField(
        max_length=20, choices=DELIVERY_STATUSES, null=True)

    def __str__(self):
        return self.delivery_status
