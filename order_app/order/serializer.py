from rest_framework import serializers
from order_app.order.models import Order

class OrderSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()
    product_description=serializers.SerializerMethodField()
    price=serializers.SerializerMethodField()
    username=serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = (
            'product_id','product_name','product_description','price','username'
        )
# customer name product_price and product description 
    def get_product_name(self, order):
        return order.product.product_title

    def get_price(self,order):
        return order.product.price

    def get_username(self,customer):
        return customer.customer.username
    
    def get_product_description(self,description):
        return description.product.product_description