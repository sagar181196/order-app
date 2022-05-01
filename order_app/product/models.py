from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

class Product(models.Model):
    product_title=models.CharField( max_length=50)
    product_description=models.CharField(max_length=200)
    price=models.IntegerField( max_length=50)