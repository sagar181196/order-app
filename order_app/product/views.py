from ast import Delete
from urllib import response
from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from order_app.product.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
import stripe
stripe.api_key = "sk_test_51Kto0HSFVfq9esEdBPrmam1DvGQmk2gn7h8tVzmzx75KNwwj46e1yvJTtCI0Q5g6469hVAmDGFy2wgIvzdRl4egG00lJ5ce2Uh"


class ProductViewSet(viewsets.ModelViewSet):
    # queryset=Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        product= Product.objects.filter(price__gte=3000000)
        print('djdjd',product)
        serializer = self.get_serializer(product,many=True)
        return Response(serializer.data)

    
class ProductDetailViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


    def put(self,request,product_id):
        product=Product.objects.filter(id=product_id).first()
        serializer = self.get_serializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,product_id):
        product=Product.objects.filter(id=product_id).first()
        if product:
            product.delete()
            return Response(data={'delete succesfully'},status=status.HTTP_202_ACCEPTED)
        return Response(data={'error':'invalid id'}, status=status.HTTP_400_BAD_REQUEST)



