from rest_framework import serializers
from .models import Actividad, Evento, Noticia, Usuario


HABILITADO: bool = True
INHABILITADO: bool = False

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'Estado', 'Correo', 'Nombre', 'Rol', 'Telefono', 'Contraseña']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['id', 'Titulo', 'Detalles', 'Estado', 'Espacio', 'Media_file', 'Fecha', 'Hora_inicio', 'Hora_finalizacion']

class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = ['Fecha', 'Hora_inicio', 'Hora_finalizacion', 'Espacio', 'Estado', 'Detalles', 'Titulo']

class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = ['Titulo', 'Descripcion', 'Resumen', 'Estado', 'Media_file', 'Fecha_edicion']

