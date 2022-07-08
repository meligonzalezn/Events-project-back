from django.db import models
from users.models import User
from events.models import Event
from cloudinary.models import CloudinaryField


class Badge(models.Model):
    ID_User = models.ForeignKey(User, on_delete=models.CASCADE)
    ID_Event = models.ForeignKey(Event, on_delete=models.CASCADE)
    Media_file = CloudinaryField(
        folder='media/images_users/', overwrite=True, resource_type='')
