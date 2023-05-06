from db.models import Product
from db.serializers.get_product_serializer import ProductSerializer
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny


# Create your view(s) here.
class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    filterset_fields = ['id', 'category']
