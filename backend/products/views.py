from rest_framework import generics, mixins #permissions #authentication
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import Product
#from ..api.permissions import IsStaffEditorPermission
from .serliaizers import ProductSerializer
#from api.authentication import TokenAuthentication
from api.mixins import StaffEditorPermissionMixin

class ProductMixinView(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                       mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer
    lookup_field = 'pk' #for retrieve, also default is pk, but change is here if required
    
    def get(self,request, *args, **kwargs): #HTTPS -> get for list and detail
        print(args, kwargs)
        pk = kwargs.get('pk') #kwargs is key-value pair
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)  
    
    def post(self, request, *args, **kwargs): #HTTPS -> post for create
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):  #also for create from before
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = 'this is created using Mixin!'
        serializer.save(content = content)
    
    
product_mixin_view = ProductMixinView.as_view()

class ProductCreateAPIView(generics.CreateAPIView): 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    #permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content = content)
    #or send a Django signal
product_create_view = ProductCreateAPIView.as_view()


class ProductDetailAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView): #from browser -> RAV of generics from DRF
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    #permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    #lookup_field = 'pk' #similar to Product.objects.get('pk') 
#this below is passed to urls.py -> products
product_detail_view = ProductDetailAPIView.as_view()



class ProductListCreateAPIView(StaffEditorPermissionMixin,generics.ListCreateAPIView): 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #below is not required after changing settings.py
    #authentication_classes = [authentication.SessionAuthentication, TokenAuthentication] 
    #from authentication.TokenAuthentication after authentication.py
    #permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission] #permissions.DjangoModelPermissions
    
    def perform_create(self, serializer):
        #email = serializer.validated_data.pop('email') #pop before save for manipulating it
        #print(email)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content = content)
    #or send a Django signal
    
    def get_queryset(self, *args, **kwargs):
        request = self.request
        print(request.user) #prints out the user when you open the page
        return super().get_queryset(*args, **kwargs)
        
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


class ProductUpdateAPIView(StaffEditorPermissionMixin, generics.UpdateAPIView): 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    lookup_field = 'pk'
    #permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]
    def perform_update(self,serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
product_update_view = ProductUpdateAPIView.as_view()


class ProductDestroyAPIView(StaffEditorPermissionMixin, generics.DestroyAPIView): 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    lookup_field = 'pk'
    #permission_classes = [IsStaffEditorPermission]
    def perform_delete(self,instance):
        super().perform_destroy(instance)
product_delete_view = ProductDestroyAPIView.as_view()