from .models import profile
from .serializers import profileSerializer, sacoleirasSerializer
from rest_framework import viewsets, permissions, authentication, filters


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
