from django import template
from testapp.models import Category,Product

register = template.Library()

@register.filter(name="getProductName")
def getProductName(value):
    getData = Category.objects.get(id=value)
    return getData.name
