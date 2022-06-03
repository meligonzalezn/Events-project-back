from rest_framework import viewsets
from .serializer import UserSerializer
from .models import Usuario


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = Usuario.objects.all()
