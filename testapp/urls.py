from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home),
    # Category API
    path('category/', views.category,name="category"),
    path('add-category/', views.addCategory,name="addCategory"),
    path('update-category/<int:id>/', views.updateCategory,name="updateCategory"),
    path('delete-category/<int:id>/', views.deleteCategory,name="deleteCategory"),
    #
    path('product/', views.product,name="product"),
    path('add-product/', views.addProduct,name="addProduct"),
    path('update-product/<int:id>/', views.updateProduct,name="updateProduct"),
    path('delete-product/<int:id>/', views.deleteProduct,name="deleteProduct"),

]