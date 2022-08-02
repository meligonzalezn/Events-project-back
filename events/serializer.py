from rest_framework import serializers
from .models import Event, Payment

class EventSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Event
        fields = ['id','Title', 'Details', 'State', 'Space', 'Cost', 'Start_date', 'Finish_date', 'Media_file']

 
class PaymentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Payment
        fields = ['ID_User', 'ID_Event', 'Date', 'Value', 'pay_method']