from .models import profile, reviews
from .serializers import profileSerializer, sacoleirasSerializer, profileVerifySerializer, reviewsSerializer, reviewsProfileMediaSerializer, rankingProfileSerializer
from rest_framework import viewsets, permissions, authentication, filters, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User      


class reviewsProfileMedia(generics.ListAPIView):
    serializer_class = reviewsProfileMediaSerializer
    
    def get_queryset(self):
        return reviews.objects.filter(profile_id=self.kwargs["pk"]).order_by('-media')
     

class rankingProfileViewSet(viewsets.ModelViewSet):
    serializer_class = rankingProfileSerializer
    queryset = profile.objects.all()
    

class haveProfile(viewsets.ModelViewSet):
    serializer_class = profileVerifySerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    
    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(id=user.id) 


class profileDetail(generics.RetrieveAPIView):
    serializer_class = profileSerializer
    queryset = profile.objects.all()


class reviewsViewSet(viewsets.ModelViewSet):
    serializer_class = reviewsSerializer
    queryset = reviews.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]


class profileViewset(viewsets.ModelViewSet):
    serializer_class = profileSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

    
    def get_queryset(self):
        user = self.request.user
        return profile.objects.filter(user=user) 


class sacoleirasViewset(viewsets.ModelViewSet):
    serializer_class = sacoleirasSerializer
    queryset = profile.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__first_name', 'user__last_name', 'state', 'city', 'district']
