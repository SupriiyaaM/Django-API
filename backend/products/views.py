from rest_framework import generics

from .models import Product
from .serliaizers import ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView): #from browser -> RAV of generics from DRF
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    #lookup_field = 'pk' #similar to Product.objects.get('pk')
    
#this below is passed to urls.py -> products
product_detail_view = ProductDetailAPIView.as_view()