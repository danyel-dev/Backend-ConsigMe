from django.contrib.auth.models import User, Group
from rest_framework import serializers
from product.models import bag


class userLogadoSerializer(serializers.HyperlinkedModelSerializer):
    fullname = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['url', 'id', 'fullname', 'profile']


    def get_fullname(self, obj):
        return f'{obj.first_name} {obj.last_name}'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['url', 'id', 'first_name', 'last_name', 'username', 'email', 'password', 'confirm_password']
        
        extra_kwargs = {
            'email': {'required': True},
            'password': {'write_only': True},
        }
    
    
    def validate_email(self, value):
        if not value.strip():  # Verifica se o valor está em branco
            raise serializers.ValidationError("O campo 'e-mail' não pode estar em branco.")
        return value
    
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        confirm_password = validated_data.pop('confirm_password')
        
        if password != confirm_password:
            raise serializers.ValidationError("As senhas não coincidem.")
        
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        
        bagUser = bag.objects.create(user=user)
        
        return user


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
