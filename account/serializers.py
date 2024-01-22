from rest_framework import serializers
from .models import profile, reviews
from django.contrib.auth.models import User


class profileSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()
    
    class Meta:
        model = profile
        fields = ['id', 'url', 'store_name', 'professional_email', 'cpf', 'birth_date', 'image', 'name', 'address', 'bio', 'phone_number']

    
    def get_name(self, obj):
        return f'{obj.user.first_name} {obj.user.last_name}'


    def get_address(self, obj):
        return f'{obj.city} {obj.state}, {obj.street} {obj.house_number} - {obj.district}, Cep {obj.cep}'


class reviewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = reviews
        fields = '__all__'


class profileVerifySerializer(serializers.HyperlinkedModelSerializer):
    HaveProfile = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['url', 'HaveProfile']

    
    def get_HaveProfile(self, obj):
        if(profile.objects.filter(user=obj).exists()):
            return True
        return False

class sacoleirasSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()
    
    class Meta:
        model = profile
        fields = ['id', 'image', 'name', 'address', 'bio', 'phone_number']

    
    def get_name(self, obj):
        return f'{obj.user.first_name} {obj.user.last_name}'


    def get_address(self, obj):
        return f'{obj.city} - {obj.state}, {obj.district}'
    