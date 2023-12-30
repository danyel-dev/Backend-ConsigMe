from rest_framework import serializers
from .models import profile


class profileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = profile
        fields = '__all__'


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
    