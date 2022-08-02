from rest_framework import serializers
from .models import Activity


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'Date', 'Init_hour', 'Final_hour', 'Space',
                  'Capacity', 'Cost', 'State', 'Details', 'Title', 'ID_Event']
