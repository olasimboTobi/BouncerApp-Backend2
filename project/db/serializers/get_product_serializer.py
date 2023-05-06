from db.models import Product
from rest_framework import serializers


# Create your serializer(s) here.
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
