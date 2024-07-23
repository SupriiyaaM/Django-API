from rest_framework import generics
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import Product
from .serliaizers import ProductSerializer

class ProductCreateAPIView(generics.CreateAPIView): 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content = content)
    #or send a Django signal
product_create_view = ProductCreateAPIView.as_view()


class ProductDetailAPIView(generics.RetrieveAPIView): #from browser -> RAV of generics from DRF
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    #lookup_field = 'pk' #similar to Product.objects.get('pk') 
#this below is passed to urls.py -> products
product_detail_view = ProductDetailAPIView.as_view()



class ProductListCreateAPIView(generics.ListCreateAPIView): 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_list_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content = content)
    #or send a Django signal
product_list_create_view = ProductListCreateAPIView.as_view()
    
    
class ProductListAPIView(generics.ListAPIView): 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer   
product_list_view = ProductListAPIView.as_view()

@api_view(['GET','POST'])
def product_alt_view(request, pk = None, *args, **kwargs):
    
    method = request.method
    if method =='GET':
        #LIST or GET -> diff on basis on url (pk)
        #get -> detail view
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj,many=False).data
            return Response(data)
        #list
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many = True).data
        return Response(data)
    
    if method == 'POST':
        #create data
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid(raise_exception = True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content = content)
            return Response(serializer.data)
        return Response({"invalid":"incorrect data."}, status = 400)

