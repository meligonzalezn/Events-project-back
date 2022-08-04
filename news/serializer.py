from rest_framework import serializers
from .models import News

class NewsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = News
        fields = ['id', 'ID_event', 'ID_user','Title', 'Description', 'Summary', 'State', 'Media_file', 'Edition_date', 'Finish_date']