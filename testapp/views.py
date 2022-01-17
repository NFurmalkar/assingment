from django.shortcuts import render,redirect
import requests
import json
from . models import Category,Product
from django.http import JsonResponse
from django.contrib import messages
# Create your views here.
def base(request):
    return render(request,'testapp/base.html')

def home(request):

    return render(request, 'testapp/home.html')

# Category View
def category(request):
    api_url = "http://127.0.0.1:8000/api/category/"
    response = requests.get(api_url)
    resData = response.json()
    params = {'resData':resData}
    return render(request, 'testapp/category.html',params)

def addCategory(request):
    if request.method == "POST":
        name = request.POST.get("name")
        api_url = "http://127.0.0.1:8000/api/category/"
        mydata = {"name": name}
        response = requests.post(api_url,data=mydata)
        print(response)
        if response.status_code == 201:
            messages.success(request,"Category Added")
        return redirect('/category')

def updateCategory(request,id):
    category = Category.objects.get(id=id)
    if request.method == "POST":
        name = request.POST.get("name")
        api_url = "http://127.0.0.1:8000/api/category/"+str(id)+"/"
        mydata = {'name': name}
        response = requests.put(api_url, data=mydata)
        print(response)
        if response.status_code == 201:
            messages.success(request,"Category Updated")
        return redirect('/category')
    params = {'category':category}
    return render(request,'testapp/category.html',params)

def deleteCategory(request,id):
    api_url = "http://127.0.0.1:8000/api/category/" + str(id) + "/"
    response = requests.delete(api_url)
    print(response)
    if response.status_code == 204:
        messages.success(request, "Category Deleted")
    return redirect('/category')

# Product View

def product(request):
    api_url = "http://127.0.0.1:8000/api/category/"
    response = requests.get(api_url)
    catData = response.json()
    # Get Product Data
    api_url = "http://127.0.0.1:8000/api/product/"
    response = requests.get(api_url)
    proData = response.json()
    params = {'catData': catData,'proData':proData}
    return render(request,'testapp/product.html',params)

def addProduct(request):
    if request.method == "POST":
        name = request.POST.get("name")
        category = request.POST.get("category")
        price = request.POST.get("price")
        desc = request.POST.get("desc")
        api_url = "http://127.0.0.1:8000/api/product/"
        mydata = {"category":category,"name": name,'price':price,'desc':desc}
        response = requests.post(api_url, data=mydata)
        print(response.json())
        if response.status_code == 201:
            messages.success(request, "Product Added")
        return redirect('/product')

def updateProduct(request,id):
    # Category Data
    api_url = "http://127.0.0.1:8000/api/category/"
    response = requests.get(api_url)
    catData = response.json()
    # Get Product Data
    api_url = "http://127.0.0.1:8000/api/product/"
    response = requests.get(api_url)
    proData = response.json()
    if request.method == "POST":
        name = request.POST.get("name")
        category = request.POST.get("category")
        price = request.POST.get("price")
        desc = request.POST.get("desc")
        api_url = "http://127.0.0.1:8000/api/product/"+str(id)+"/"
        mydata = {"category":category,"name": name,'price':price,'desc':desc}
        response = requests.put(api_url, data=mydata)
        print(response)
        if response.status_code == 200:
            messages.success(request, "Product Updated")
        return redirect('/product')
    params = {'catData':catData,'proData': proData}
    return render(request, 'testapp/product.html', params)

def deleteProduct(request,id):
    api_url = "http://127.0.0.1:8000/api/product/"+str(id)+"/"
    response = requests.delete(api_url)
    print(response.status_code)
    if response.status_code == 204:
        messages.success(request, "Product Deleted")
    return redirect('/product')


