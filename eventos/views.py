from urllib.request import Request
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .serializer import ActividadSerializer, EventSerializer, NoticiaSerializer, UserSerializer
from .models import Usuario, Evento, Usuario, Actividad, Pago, Noticia
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class UserViewSet(viewsets.ModelViewSet):

    model = Usuario
    serializer_class = UserSerializer
    queryset = Usuario.objects.all()

    http_method_names = ['get', 'post', 'put']

    
    @action(detail=True, methods=['get'], url_path='watch')
    ## 
    def get_user(self: object, request: Request, pk: int):
        try:
            query = Usuario.objects.all().get(pk=pk)
            serializer: UserSerializer = self.serializer_class(query, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response("User doesn't exist", status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['put'], url_path='update')
    def actualizar(this, request, pk):
        try:
            user = Usuario.objects.get(id=pk)
            
            if('Nombre' in request.data):
                user.Nombre = request.data['Nombre']
            if('Estado' in request.data):
                user.Estado = request.data['Estado']
            if('Rol' in request.data):
                user.Rol = request.data['Rol'] 
            if('Correo' in request.data):
                user.Correo = request.data['Correo']
            if('Telefono' in request.data):
                user.Telefono = request.data['Telefono']
            if('Contraseña' in request.data):
                user.Contraseña = request.data['Contraseña']
            user.save()

            return Response("User " + pk + " updated", status=status.HTTP_200_OK)
        except:
            return Response("Error", status.HTTP_500_INTERNAL_SERVER_ERROR)

    # @action(detail=True, methods={'post'})
    # def gl():
    @action(detail=True, methods=['get'], url_path='habilitar')
    def habilitar(this, _, pk):
        # try:
            user = Usuario.objects.get(id=pk)
            user.Estado = not user.Estado
            user.save()
            
            return Response("Usuario" + user.Nombre + "Actualizado", status=status.HTTP_200_OK)
        # except:
        #     return Response("Error", status.HTTP_400_BAD_REQUEST)

class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Evento.objects.all()


class ActividadViewSet(viewsets.ModelViewSet):
    serializer_class = ActividadSerializer
    queryset = Actividad.objects.all()


class NoticiaViewSet(viewsets.ModelViewSet):
    serializer_class = NoticiaSerializer
    queryset = Noticia.objects.all()
