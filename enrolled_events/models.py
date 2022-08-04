from django.db import models
from users.models import User
from events.models import Event


class Enroll(models.Model):
    ID_User = models.ForeignKey(User, on_delete=models.CASCADE)
    ID_Event = models.ForeignKey(Event, on_delete=models.CASCADE)
    Date = models.DateField()
