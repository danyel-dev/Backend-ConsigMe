from .models import profile
from .serializers import profileSerializer, sacoleirasSerializer
from rest_framework import viewsets, permissions, authentication, filters, generics


class profile(generics.ListAPIView):
    serializer_class = profileSerializer
        
    def get_queryset(self):
        return profile.objects.filter(user_id=self.kwargs['id']) 


class sacoleirasViewset(viewsets.ModelViewSet):
    serializer_class = sacoleirasSerializer
    queryset = profile.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__first_name', 'user__last_name', 'state', 'city', 'district']
