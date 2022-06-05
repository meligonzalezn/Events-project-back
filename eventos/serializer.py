from rest_framework import serializers
from .models import Actividad, Evento, Noticia, Usuario


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['Nombre', 'Correo', 'Rol', 'Estado']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        field = ['Titulo', 'Detalles', 'Estado', 'Espacio', 'Media_file', 'Fecha', 'Hora_inicio', 'Hora_finalizacion']

class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        field = ['Fecha', 'Hora_inicio', 'Hora_finalizacion', 'Espacio', 'Estado', 'Detalles', 'Titulo']

class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        field = ['Titulo', 'Descripcion', 'Resumen', 'Estado', 'Media_file', 'Fecha_edicion']

