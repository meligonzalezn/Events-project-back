from django.db import models
# Create your models here.

class User(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=120)
    State = models.BooleanField(default=True)
    Role = models.CharField(max_length=50)
    Email = models.CharField(max_length=500)
    Password = models.CharField(max_length=255)

class Event(models.Model):
    ID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100)
    Details = models.CharField(max_length=50)
    State = models.CharField(max_length=20)
    Space = models.CharField(max_length=20)
    Media_file = models.ImageField(upload_to='images_events/')
    Date = models.DateField()
    Init_hour = models.TimeField()
    Final_hour = models.TimeField()

class Activity(models.Model):
    ID = models.AutoField(primary_key=True)
    Date = models.DateField()
    Init_hour = models.TimeField()
    Final_hour = models.TimeField()
    Space = models.CharField(max_length=100)
    State = models.CharField(max_length=50)
    Details = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    ID_Event = models.ForeignKey(Event, on_delete=models.CASCADE)

    
class Payment(models.Model):
    ID = models.AutoField(primary_key=True)
    Date = models.DateField()
    Value = models.IntegerField()
    pay_method = models.CharField(max_length=30)

class News(models.Model):
    ID = models.AutoField(primary_key=True)
    ID_EVENT = models.ForeignKey(Event, on_delete=models.CASCADE)
    ID_USER = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=100)
    Description = models.TextField()
    Summary = models.CharField(max_length=255)
    State = models.CharField(max_length=20)
    #El campo para subir las imágenes o videos
    Media_file = models.ImageField(upload_to='images_videos_news/')
    Edition_date = models.DateField()

class event_payments(models.Model):
    ID_User = models.ForeignKey(User, on_delete=models.CASCADE)
    ID_Payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    ID_Event = models.ForeignKey(Event, on_delete=models.CASCADE)

class Enrolled_in_activity(models.Model):
    ID_user = models.ForeignKey(User, on_delete=models.CASCADE)
    ID_activity = models.ForeignKey(Activity, on_delete= models.CASCADE)