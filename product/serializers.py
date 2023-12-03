from rest_framework import serializers
from .models import product, message, bag, comment
from django.contrib.auth.models import User
from setup.serializers import UserSerializer


class commentSerializer(serializers.HyperlinkedModelSerializer):
    full_name = serializers.SerializerMethodField()
    initial_letters = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
     
    
    class Meta:
        model = comment
        fields = ['id', 'url', 'user', 'product', 'full_name', 'initial_letters', 'message', 'created_at']
    
    
    extra_kwargs = {
        'user': {'write_only': True},
        'product': {'write_only': True},
    }
    
    
    def get_full_name(self, obj):
        return f'{obj.user.first_name} {obj.user.last_name}'
    
    
    def get_initial_letters(self, obj):
        return f'{obj.user.first_name[0]}{obj.user.last_name[0]}' 
    
     
    def get_created_at(self, obj):
        return f'{obj.created_at.strftime("%d/%m/%Y")} ás {obj.created_at.strftime("%H:%M")}'
    
        
class productSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    comment_set = commentSerializer(many=True)
    
    class Meta:
        model = product
        fields = ['id', 'url', 'comment_set', 'user', 'image', 'description', 'name', 'value', 'size', 'quantity']
    

class BagProductSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.CharField()
    fullname = serializers.SerializerMethodField()
    
     
    class Meta:
        model = product
        fields = ['image', 'user', 'fullname', 'value', 'size', 'name', 'quantity']


    def get_fullname(self, obj):
        return f'{obj.user.first_name} {obj.user.last_name}'


class bagSerializer(serializers.HyperlinkedModelSerializer):    
    products = BagProductSerializer(many=True)
    
    class Meta:
        model = bag
        fields = ['id', 'url', 'user', 'products']
    
    
    def update(self, instance, validated_data):
        new_products_data = validated_data.get('products', [])

        # Adicione novos produtos à lista existente
        for new_product_data in new_products_data:
            new_product_data.pop('id', None)  # Remova o ID, pois é um novo produto
            instance.products.create(**new_product_data)
        
        return instance
        
        # new_product = { 
        #     "image": "aaaaaaaa",
        #     "user": "http://127.0.0.1:8000/users/48/",
        #     "fullname": "Carlos daniel Pinheiro",
        #     "value": 34.50,
        #     "size": "M",
        #     "name": "Camisa Regata",
        #     "quantity": 3
        # }
        
        # instance.id = 22
        # instance.url = "http://127.0.0.1:8000/users/48/"
        # instance.products.set([])
        # instance.save()
        
        # return instance
    
    
class messageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = message
        fields = ['id', 'url', 'title', 'email', 'message', 'created_at' ,'updated_at']


class searchSacoleirasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email']


class sacoleiraProductsSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = product
        fields = ['id', 'user', 'image', 'description', 'name', 'value', 'size', 'quantity']


class productDetailSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
        
    class Meta:
        model = product
        fields = ['id', 'image', 'description', 'name', 'value', 'size', 'quantity', 'user']
