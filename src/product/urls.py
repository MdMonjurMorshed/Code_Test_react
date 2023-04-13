from django.urls import path
from django.views.generic import TemplateView

from product.views.product import CreateProductView,ProductList,SerialView,ProductSerial,VariantSerial,tableData
from product.views.variant import VariantView, VariantCreateView, VariantEditView

app_name = "product"

urlpatterns = [
    # Variants URLs
    path('variants/', VariantView.as_view(), name='variants'),
    path('variant/create', VariantCreateView.as_view(), name='create.variant'),
    path('variant/<int:id>/edit', VariantEditView.as_view(), name='update.variant'),

    # Products URLs
    path('create/', CreateProductView.as_view(), name='create.product'),
    path('list/', TemplateView.as_view(template_name='products/list.html', extra_context={
        'product': True
    }), name='list.product'),
    path('product-list/',ProductList.as_view(),name='product_list.product'),
    
    path('product-api/',SerialView.as_view(),name="product.api"),
    path('product-list-api/',ProductSerial.as_view(),),
    path('var-api/',VariantSerial.as_view(),),
    path('data/',tableData,name='product.data'),
    
]
