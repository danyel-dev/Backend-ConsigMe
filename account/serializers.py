from rest_framework import serializers
from .models import profile, reviews, lojista
from django.contrib.auth.models import User
from drf_extra_fields.fields import Base64ImageField


class lojistaSerializer(serializers.HyperlinkedModelSerializer):
    image = Base64ImageField()
    
    class Meta:
        model = lojista
        fields = ['id', 'url', 'name', 'description', 'proprietario', 'email', 'phone_number', 'image', 'cnpj', 'cep', 'state', 'city','district', 'street', 'number', 'complement']


class lojistaDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = lojista
        fields = '__all__'


class reviewsProfileMediaSerializer(serializers.HyperlinkedModelSerializer):
    # media = serializers.SerializerMethodField()
    
    class Meta:
        model = reviews
        fields = '__all__'
        
        
    # def get_media(self, instace):
    #     pk = self.context['view'].kwargs.get('pk') 
    #     soma_das_notas = sum(reviews.objects.filter(profile=7).values_list('note', flat=True))
    #     qtd_notas = reviews.objects.filter(profile=7).count()
    #     print(qtd_notas)
    #     if(qtd_notas == 0):
    #         return 0
    #     return round(soma_das_notas/qtd_notas, 2)
        

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


class rankingProfileSerializer(serializers.HyperlinkedModelSerializer):
    avaliacao = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()
        
    class Meta:
        model = profile
        fields = ['id', 'url', 'name', 'image', 'avaliacao', 'phone_number', 'address']


    def get_name(self, obj):
        return f'{obj.user.first_name} {obj.user.last_name}'


    def get_address(self, obj):
        return f'{obj.street} {obj.house_number}, {obj.city} - {obj.state}'


    def get_avaliacao(self, instance):
        soma_das_notas = sum(reviews.objects.filter(profile=instance.id).values_list('note', flat=True))
        qtd_notas = reviews.objects.filter(profile=instance.id).count()
        return round(soma_das_notas/qtd_notas, 2)


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
    # name = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()
    
    class Meta:
        model = profile
        fields = ['id', 'url', 'image', 'address', 'bio', 'phone_number']

    
    # def get_name(self, obj):
    #     return f'{obj.user.first_name} {obj.user.last_name}'


    def get_address(self, obj):
        return f'{obj.city} - {obj.state}, {obj.district}'
    