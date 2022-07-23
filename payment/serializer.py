from rest_framework import serializers
from .models import Badge


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = ['id', 'ID_User', 'ID_Event', 'Media_file']
