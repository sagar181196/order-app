from order_app.product.models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    
    
    
    class Meta:
        model = Product
        fields = [ 'product_title','product_description','price']

