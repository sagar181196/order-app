from django.db import models
from order_app.customer.models import Customer
from order_app.product.models import Product

class Order(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)