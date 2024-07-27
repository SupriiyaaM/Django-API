from rest_framework import mixins, viewsets
from .models import Product
from .serliaizers import ProductSerializer

class ProductViewSets(viewsets.ModelViewSet):
    '''
    get -> list and retrieve
    post -> create New Instance
    put -> Update
    patch -> Partial Update
    delete -> destroy
    '''
    queryset= Product.objects.all()
    serializer_class= ProductSerializer
    lookup_field = 'pk'
    
#below can be used only for get methods
class ProductGenericViewSets(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                             viewsets.GenericViewSet):
    '''
    get -> list and retrieve
    '''
    queryset= Product.objects.all()
    serializer_class= ProductSerializer
    lookup_field = 'pk'