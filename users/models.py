from django.db import models
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.


class User(models.Model):
    Name = models.CharField(max_length=60)
    Last_name = models.CharField(max_length=60, default='')
    State = models.BooleanField(default=True)
    Role = models.CharField(max_length=51)
    Email = models.CharField(max_length=510)
    Password = models.CharField(max_length=255)
    Phone = models.CharField(max_length=16, default='')
    Media_file = cloudinary.models.CloudinaryField(
        folder='media/images_users/', overwrite=True, resource_type='')

    def check_password(this, password):
        if(this.Password == password and this.State is True):
            return True
        return False
