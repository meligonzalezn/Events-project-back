from rest_framework import serializers
from .models import Enroll


class EnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enroll
        fields = ['ID_User', 'ID_Event', 'Date']
