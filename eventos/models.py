from django.db import models

# Create your models here.


class Usuario(models.Model):
    Nombre = models.CharField(max_length=120)
    Estado = models.BooleanField(default=True)
    Rol = models.CharField(max_length=50)
    Correo = models.CharField(max_length=100, unique=True)
    Telefono = models.CharField(max_length=16, default='')
    Contraseña = models.CharField(max_length=255)


class Evento(models.Model):
    Titulo = models.CharField(max_length=100)
    Detalles = models.CharField(max_length=50)
    Estado = models.CharField(max_length=20)
    Espacio = models.CharField(max_length=20)
    Media_file = models.CharField(max_length=100)
    Fecha = models.DateField()
    Hora_inicio = models.TimeField()
    Hora_finalizacion = models.TimeField()


class Actividad(models.Model):
    Fecha = models.DateField()
    Hora_inicio = models.TimeField()
    Hora_finalizacion = models.TimeField()
    Espacio = models.CharField(max_length=100)
    Estado = models.CharField(max_length=50)
    Detalles = models.CharField(max_length=100)
    Titulo = models.CharField(max_length=100)
    ID_Evento = models.ForeignKey(Evento, on_delete=models.CASCADE)


class Pago(models.Model):
    Fecha = models.DateField()
    Valor = models.IntegerField()
    Metodo = models.CharField(max_length=30)


class Noticia(models.Model):
    ID_EVENTO = models.ForeignKey(Evento, on_delete=models.CASCADE)
    # El usuario es para saber quien cró la noticia?
    ID_USUARIO = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Titulo = models.CharField(max_length=100)
    Descripcion = models.TextField()
    Resumen = models.CharField(max_length=255)
    Estado = models.CharField(max_length=20)
    Media_file = models.CharField(max_length=200)
    Fecha_edicion = models.DateField()


class Pago_de_evento(models.Model):
    ID_Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    ID_Pago = models.ForeignKey(Pago, on_delete=models.CASCADE)
    ID_Evento = models.ForeignKey(Evento, on_delete=models.CASCADE)


class Inscritos_a_actividad(models.Model):
    ID_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    ID_Actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
