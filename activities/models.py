from django.db import models
from events.models import Event

# Create your models here.
class Activity(models.Model):
    Date = models.DateField()
    Init_hour = models.TimeField()
    Final_hour = models.TimeField()
    Space = models.CharField(max_length=100)
    State = models.CharField(max_length=51)
    Details = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    ID_Event = models.ForeignKey(Event, on_delete=models.CASCADE)