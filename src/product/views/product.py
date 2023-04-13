from django.views import generic
from rest_framework.generics import ListAPIView
from product.models import Variant,ProductVariantPrice,Product,ProductVariant
from django.http import JsonResponse
from rest_framework import request
from product.serializers import ProductVariantPrice_selializer,ProductSerializer,VariantSerializer
import json


class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context
class ProductList (generic.ListView):
    model=ProductVariantPrice
    template_name='products/list.html'
    paginate_by=10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product"] =Product.objects.all() 
        context["variant"]=ProductVariant.objects.all()
       
        return context
def tableData(request):
    pro=Product.objects.all()
    
    pro_data=[{"id":i.id,"title":i.title}for i in pro]
    pro_var=ProductVariant.objects.all()
    
    pro_var_data=[{"id":i.id,"variant":i.variant_id,"varient_title":i.variant_title,"product":i.product_id} for i in pro_var]
    
    pro_var_price=ProductVariantPrice.objects.all()
    pro_var_price_data=[{"id": i.id,"product":i.product_id,"var_one":i.product_variant_one_id,"var_two":i.product_variant_two_id,"var_three":i.product_variant_three_id,'price':i.price,'stock':i.stock} for i in pro_var_price ]
    collected_data={ "product":pro_data,
        "product_variant":pro_var_data,
        "product_var_price":pro_var_price_data}
       
    print(collected_data)
        
    return JsonResponse(collected_data,safe=False)
    

class SerialView(ListAPIView):
    queryset=ProductVariantPrice.objects.all()
    serializer_class=ProductVariantPrice_selializer
    
class ProductSerial(ListAPIView):
    queryset=Product.objects.all()
    serializer_class=   ProductSerializer 
    
class VariantSerial(ListAPIView):
    queryset=Variant.objects.all()
    serializer_class=VariantSerializer    
    
    
        