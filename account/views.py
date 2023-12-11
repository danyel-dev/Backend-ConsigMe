from .models import profile
from .serializers import profileSerializer
from rest_framework import viewsets, permissions, authentication


class profileViewset(viewsets.ModelViewSet):
    serializer_class = profileSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

    
    def get_queryset(self):
        user = self.request.user
        return profile.objects.filter(user=user) 
