from rest_framework import serializers
from product.models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"
        
class Serializevariant(serializers.ModelSerializer):
    class Meta:
        model=Variant
        fields="__all__"        
class VariantSerializer(serializers.ModelSerializer):
    product=ProductSerializer()
    variant=Serializevariant()
    class Meta:
        model=ProductVariant
        fields="__all__"
class ProductVariantPrice_selializer(serializers.ModelSerializer):
    product=ProductSerializer()
    product_variant_one=VariantSerializer()
    product_variant_two=VariantSerializer()
    product_variant_three=VariantSerializer()
 
    class Meta:
        model=ProductVariantPrice
        fields="__all__"