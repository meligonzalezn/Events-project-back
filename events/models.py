from django.db import models    
# from activities.models import Activity
from users.models import User

import cloudinary
from cloudinary.models import CloudinaryField
# Create your models here.


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





class Payment(models.Model):
    ID_User = models.ForeignKey(User, on_delete=models.CASCADE)
    ID_Event = models.ForeignKey(Event, on_delete=models.CASCADE)
    Date = models.DateField()
    Value = models.IntegerField()
    pay_method = models.CharField(max_length=30)




# class Enrolled_in_activity(models.Model):
#     ID_user = models.ForeignKey(User, on_delete=models.CASCADE)
#     ID_activity = models.ForeignKey(Activity, on_delete=models.CASCADE)

