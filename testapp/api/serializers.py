from rest_framework.serializers import ModelSerializer,Serializer
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from testapp.models import Category,Product


class categorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class productSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

