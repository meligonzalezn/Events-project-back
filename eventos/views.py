from rest_framework import viewsets
from .serializer import ActividadSerializer, EventSerializer, NoticiaSerializer, UserSerializer
from .models import Usuario, Evento, Usuario, Actividad, Pago, Noticia


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = Usuario.objects.all()

class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Evento.objects.all()

class ActividadViewSet(viewsets.ModelViewSet):
    serializer_class = ActividadSerializer
    queryset = Actividad.objects.all()

class NoticiaViewSet(viewsets.ModelViewSet):
    serializer_class = NoticiaSerializer
    queryset = Noticia.objects.all()
    

