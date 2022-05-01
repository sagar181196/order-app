from telnetlib import STATUS
from django.shortcuts import render
from .models import Order,Product
from order_app.order.models import Order
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from order_app.order.serializer import OrderSerializer
from rest_framework.permissions import IsAuthenticated


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


    def get(self,request):
        queryset=Order.objects.select_related('customer').filter(customer_id=request.user.id).filter(product__product_title__icontains=request.GET["search"])
        # queryset=Order.objects.select_related('customer').filter(customer_id=.GET)
        serializer= self.get_serializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK )

    def post(self,request):
        queryset=Order.objects.create(product_id=request.data['product_id'],customer_id=request.user.id)
        re = {
            'product_title' : queryset.product.product_title,
            'customer_username' : queryset.customer.username
        }
        return Response(re, status=status.HTTP_201_CREATED)

    
    def delete(self,request):
        queryset=Order.objects.filter(id=request.data['order_id'])
        if queryset:
            queryset.delete()
            return Response('deleted succesfully',status=status.HTTP_200_OK )
        return Response('invalid',status=status.HTTP_400_BAD_REQUEST)


