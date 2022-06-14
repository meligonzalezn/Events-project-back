from rest_framework import serializers
from .models import News

class NewsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = News
        fields = ['ID_event', 'ID_user','Title', 'Description', 'Summary', 'State', 'Media_file', 'Edition_date']
