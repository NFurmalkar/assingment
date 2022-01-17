from django.db import models
import datetime

# Create your models here.
class Category(models.Model):
    date = models.DateTimeField(default=datetime.datetime.today())
    name = models.CharField(max_length=100,default="")
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="")
    price = models.IntegerField(null=True)
    desc = models.TextField(null=True)
