from django.db import models
from users.models import User
from events.models import Event
from activities.models import Activity


class Payment(models.Model):
    ID_User = models.ForeignKey(User, on_delete=models.CASCADE)
    ID_Event = models.ForeignKey(Event, on_delete=models.CASCADE)
    ID_Activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    Date = models.DateField()
    Value = models.IntegerField()
    pay_method = models.CharField(max_length=30)
