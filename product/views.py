from rest_framework import viewsets, generics
from .models import product, message, bag, comment, product
from .serializers import productSerializer, messageSerializer, bagSerializer, sacoleiraProductsSerializer, searchSacoleirasSerializer, commentSerializer
from rest_framework import permissions, authentication
from django.contrib.auth.models import User
from rest_framework.parsers import MultiPartParser, FormParser


class productViewSet(viewsets.ModelViewSet):
    queryset = product.objects.all()
    serializer_class = productSerializer


class messageViewSet(viewsets.ModelViewSet):
    queryset = message.objects.all()
    serializer_class = messageSerializer
    

class bagViewSet(viewsets.ModelViewSet):
    serializer_class = bagSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

    
    def get_queryset(self):
        user = self.request.user
        return bag.objects.filter(user=user)


class sacoleiraProducts(generics.ListAPIView):
    serializer_class = sacoleiraProductsSerializer
    
    def get_queryset(self):
        return product.objects.filter(user_id=self.kwargs['id'])


class commentViewset(viewsets.ModelViewSet):
    queryset = comment.objects.all().order_by('-created_at')
    serializer_class = commentSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    