from django.db import models

# Create your models here.


class Usuario(models.Model):
    Nombre = models.CharField(max_length=120)
    Estado = models.BooleanField(default=True)
    Rol = models.CharField(max_length=50)
    Correo = models.CharField(max_length=100)
    Contraseña = models.CharField(max_length=255)
