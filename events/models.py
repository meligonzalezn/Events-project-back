from django.db import models
from users.models import User


class Event(models.Model):
    Title = models.CharField(max_length=100)
    Details = models.CharField(max_length=500, blank=True, null=True)
    State = models.CharField(max_length=20)
    Space = models.CharField(max_length=200, blank=True, null=True)
    Cost = models.IntegerField(default=0)
    Media_file = models.ImageField(
        upload_to='images_events/', blank=True, null=True)
    Start_date = models.DateField()
    Finish_date = models.DateField()
