from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Product

# def validate_title(self, value):
#         qs = Product.objects.filter(title__iexact = value) #case insensitive 
#         if qs.exists():
#             raise serializers.ValidationError(f"{value} is alredy a product name. Enter another title.")
#         return value

def validate_title_no_hello(value):
    if "hello" in value.lower():
        raise serializers.ValidationError(f"Hello is not allowed as a title.")
    return value

unique_product_title = UniqueValidator(queryset= Product.objects.all()) #not case insensitive


