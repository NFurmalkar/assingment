from testapp.api.serializers import categorySerializer,productSerializer
from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView,ListAPIView,RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django import http
from testapp.models import Category,Product

# Category By Using APIView
class category(APIView):
    def get(self,request):
        categoryData = Category.objects.all()
        serializer = categorySerializer(categoryData,many=True)
        return Response(serializer.data)

    def post(self, request):
        json_data = request.data
        serializer = categorySerializer(data=json_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':"data Added"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

class categoryDetails(APIView):
    def put(self,request,pk):
        qs = Category.objects.get(id=pk)
        serializer = categorySerializer(qs,data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response({'message': "data Added"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    def delete(self,request,pk):
        qs = Category.objects.get(id=pk)
        qs.delete()
        return Response({"message":"category Deleted"},status=status.HTTP_204_NO_CONTENT)

# product by using Generics

class product_LC(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = productSerializer
class product_RUD(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = productSerializer