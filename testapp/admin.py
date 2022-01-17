from django.contrib import admin
from .models import Category,Product

# Register your models here.
class categoryAdmin(admin.ModelAdmin):
    list_display = ['id','date','name']
class productyAdmin(admin.ModelAdmin):
    list_display = ['id','category','name','price','desc']

admin.site.register(Category,categoryAdmin)
admin.site.register(Product,productyAdmin)