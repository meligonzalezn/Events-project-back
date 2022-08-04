from django.db import models
from events.models import Event
from users.models import User
import cloudinary
from cloudinary.models import CloudinaryField
# Create your models here.


class News(models.Model):
    ID_event = models.ForeignKey(Event, on_delete=models.CASCADE)
    ID_user = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=100)
    Description = models.TextField()
    Summary = models.CharField(max_length=255)
    State = models.CharField(max_length=20)
    Media_file = cloudinary.models.CloudinaryField(
        folder='media/images_videos_news/', overwrite=True, resource_type='')
    Edition_date = models.DateField()
    Finish_date = models.DateField()