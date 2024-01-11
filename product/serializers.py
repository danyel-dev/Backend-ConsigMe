from rest_framework import serializers
from .models import product, message, bag, ProductNote
from django.contrib.auth.models import User
from setup.serializers import UserSerializer
from drf_extra_fields.fields import Base64ImageField


class productNoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductNote
        fields = ['id', 'url', 'user', 'product', 'note']


class productSerializer(serializers.HyperlinkedModelSerializer):
    fullname = serializers.SerializerMethodField()
    image = Base64ImageField()
    
    class Meta:
        model = product
        fields = ['id', 'url', 'fullname', 'sacoleira', 'image', 'description', 'name', 'value', 'size', 'quantity']
        
    
    def get_fullname(self, obj):
        return f'ricardo'

    
class bagSerializer(serializers.HyperlinkedModelSerializer):    
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
    productnote_set = productNoteSerializer(many=True, read_only=True)
    
    class Meta:
        model = product
        fields = ['id', 'sacoleira', 'productnote_set', 'image', 'description', 'name', 'value', 'size', 'quantity']
    

class productDetailSerializer(serializers.HyperlinkedModelSerializer):
    productnote_set = productNoteSerializer(many=True, read_only=True)
    
    class Meta:
        model = product
        fields = ['id', 'url', 'productnote_set', 'image', 'description', 'name', 'value', 'size', 'quantity']
