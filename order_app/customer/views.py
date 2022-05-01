from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from order_app.serializers import UserSerializer
from order_app.customer.models import Customer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
# from rest_framework.permissions import IsAuthenticated
import stripe
stripe.api_key = "sk_test_51Kto0HSFVfq9esEdBPrmam1DvGQmk2gn7h8tVzmzx75KNwwj46e1yvJTtCI0Q5g6469hVAmDGFy2wgIvzdRl4egG00lJ5ce2Uh"


class UserViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]


    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    def post(self,request):
        if not "username" in request.data:
            return Response(data={'error':'username is required'},status=status.HTTP_400_BAD_REQUEST)
        queryset=Customer.objects.filter(username=request.data['username']).first()
        if queryset.check_password(request.data.get('password')):
            serializer = self.get_serializer(queryset)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(data={'error':'invalid username and password'},status=status.HTTP_400_BAD_REQUEST)
        

class Logout(viewsets.ModelViewSet):
    def post(self,request):
        token=Token.objects.filter(user_id=request.user.id)
        if token:
            token.delete()
            return Response(status=status.HTTP_200_OK)




class StripeViewSet(viewsets.ModelViewSet):
    def post(self,request):
        # customer=stripe.Customer.create(
        #         description="sagar",
        #         )

        # stripe.Customer.create_source(
        #         customer.id,
        #         source="tok_visa",
        #         )

        payment=stripe.PaymentIntent.create(
                amount=2000,
                currency="usd",
                payment_method_types=["card"],
                confirm=True,
                customer="cus_Lb3gc97ow60bkI"
                )

        # stripe.PaymentIntent.confirm(
        #         payment.id,
        #         payment_method="pm_card_visa",
                
        #         )
        return Response(status=status.HTTP_201_CREATED)