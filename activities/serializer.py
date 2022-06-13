from rest_framework import serializers
from .models import Activity

class ActivitySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Activity
        fields= ['Date', 'Init_hour', 'Final_hour', 'Space', 'State', 'Details', 'Title' ]