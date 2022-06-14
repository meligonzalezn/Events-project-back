from django.db import models

# Create your models here.
class User(models.Model):
    Name = models.CharField(max_length=120)
    State = models.BooleanField(default=True)
    Role = models.CharField(max_length=51)
    Email = models.CharField(max_length=510)
    Password = models.CharField(max_length=255)
    Phone = models.CharField(max_length=16, default='')
    
    def check_password(this, password):
        if(this.Password == password and this.State is True):
            return True
        return False