from rest_framework import serializers
from .models import profile


class profileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = profile
        fields = '__all__'
