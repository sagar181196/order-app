# from django.contrib.auth.models import Customer
from order_app.customer.models import Customer
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    token=serializers.SerializerMethodField()
    
    class Meta:
        model = Customer
        fields = ['username','password','email', 'first_name','token']
        # extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)
       


    def get_token(self,obj):
        token,created=Token.objects.get_or_create(user_id=obj.id)
        # validated_data['password'] = make_password(validated_data['password'])
        return token.key

