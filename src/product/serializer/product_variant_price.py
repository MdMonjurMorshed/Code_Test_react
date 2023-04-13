from rest_framework import serializers
from product.models import *

class ProductVariantPrice_selializer(serializers.ModelSerializer):
    class Meta:
        model=ProductVariantPrice
        fields="__all__"