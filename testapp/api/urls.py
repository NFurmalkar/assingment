from django.contrib import admin
from django.urls import path,include
from testapp.api import views

urlpatterns = [
    path('category/', views.category.as_view()),
    path('category/<pk>/', views.categoryDetails.as_view()),
    # Product
    path('product/', views.product_LC.as_view()),
    path('product/<pk>/', views.product_RUD.as_view()),

]