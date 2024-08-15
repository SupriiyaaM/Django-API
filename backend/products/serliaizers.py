from rest_framework import  serializers 
from rest_framework.reverse import reverse 
from . import validators
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only = True)
    edit_url = serializers.SerializerMethodField(read_only = True)
    url = serializers.HyperlinkedIdentityField(view_name='product-detail',lookup_field= 'pk')
    #email = serializers.EmailField(write_only = True)
    title = serializers.CharField(validators = [validators.unique_product_title,
                                                validators.validate_title_no_hello])
    #repeat_title = serializers.CharField(source = 'title', read_only = True)
    class Meta:
        model = Product
        fields = [#'user',
                  'url','edit_url','id',
                  #'repeat_title', 
                  'title','content', 'price', 'sale_price','my_discount']
        
        
    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__iexact = value) #case insensitive 
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is alredy a product name. Enter another title.")
    #     return value


    #over writing the default create method
    #def create(self, validated_data):
        #email = validated_data.pop('email')
        #obj = super().create(validated_data)
        #print(email,obj)
        #return obj
        #return Product.object.create(**validated_data)
        #back to def perform create in views
    
    #def update(self, instance, validated_data):
    #   email = validated_data.pop('email')
    #   return super().update(instance, validated_data)

    def get_edit_url(self, obj):
        # get request from serializer -> 
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit", kwargs={'pk': obj.pk}, request = request)


    def get_my_discount(self,obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
         