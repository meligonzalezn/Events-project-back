from turtle import title
from django.db import models    
import cloudinary
from cloudinary.models import CloudinaryField
# Create your models here.


class User(models.Model):
    Name = models.CharField(max_length=120)
    State = models.BooleanField(default=True)
    Role = models.CharField(max_length=51)
    Email = models.CharField(max_length=510)
    Password = models.CharField(max_length=255)
    Phone = models.CharField(max_length=16, default='')


class Event(models.Model):
    Title = models.CharField(max_length=100)
    Details = models.CharField(max_length=51, blank=True, null=True)
    State = models.CharField(max_length=20)
    Space = models.CharField(max_length=20)
    Cost = models.IntegerField(default=0)
    ##images_events/
    Media_file = cloudinary.models.CloudinaryField(folder='media/images_videos_news/', overwrite=True, resource_type='')
    Start_date = models.DateField()
    Finish_date = models.DateField()


class Activity(models.Model):
    Date = models.DateField()
    Init_hour = models.TimeField()
    Final_hour = models.TimeField()
    Space = models.CharField(max_length=100)
    State = models.CharField(max_length=51)
    Details = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    ID_Event = models.ForeignKey(Event, on_delete=models.CASCADE)


class Payment(models.Model):
    ID_User = models.ForeignKey(User, on_delete=models.CASCADE)
    ID_Event = models.ForeignKey(Event, on_delete=models.CASCADE)
    Date = models.DateField()
    Value = models.IntegerField()
    pay_method = models.CharField(max_length=30)


class News(models.Model):
    ID_event = models.ForeignKey(Event, on_delete=models.CASCADE)
    ID_user = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=100)
    Description = models.TextField()
    Summary = models.CharField(max_length=255)
    State = models.CharField(max_length=20)
    Media_file = cloudinary.models.CloudinaryField(folder='media/images_videos_news/', overwrite=True, resource_type='')
    Edition_date = models.DateField()


class Enrolled_in_activity(models.Model):
    ID_user = models.ForeignKey(User, on_delete=models.CASCADE)
    ID_activity = models.ForeignKey(Activity, on_delete=models.CASCADE)

