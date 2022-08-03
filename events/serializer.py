from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Event
        fields = ['id','Title', 'Details', 'State', 'Space', 'Cost', 'Start_date', 'Finish_date', 'Media_file']