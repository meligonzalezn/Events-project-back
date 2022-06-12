from rest_framework import serializers
from .models import User, Event, Activity, News

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'Name', 'Phone', 'Email', 'Role', 'State', 'Password']

class EventSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Event
        fields = ['Title', 'Details', 'State', 'Space', 'Media_file', 'Date', 'Init_hour', 'Final_hour']

class ActivitySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Activity
        fields= ['Date', 'Init_hour', 'Final_hour', 'Space', 'State', 'Details', 'Title' ]

class NewsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = News
        fields = ['ID_event', 'ID_user','Title', 'Description', 'Summary', 'State', 'Media_file', 'Edition_date']
