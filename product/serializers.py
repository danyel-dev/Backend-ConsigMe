from rest_framework import serializers
from .models import product, message, bag, comment
from django.contrib.auth.models import User
from setup.serializers import UserSerializer


class commentSerializer(serializers.HyperlinkedModelSerializer):
    full_name = serializers.SerializerMethodField()
    initial_letters = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format='%d/%m/%Y %H:%M', read_only=True)
     
    
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
    
        
class productSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    comment_set = commentSerializer(many=True)
    
    class Meta:
        model = product
        fields = ['id', 'url', 'comment_set', 'user', 'image', 'description', 'name', 'value', 'size', 'quantity']


class bagSerializer(serializers.HyperlinkedModelSerializer):
    # products = productSerializer(many=True)
    
    class Meta:
        model = bag
        fields = ['id', 'url', 'user', 'products']


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
