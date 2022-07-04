from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'Name', 'Last_name', 'Phone', 'Email',
                  'Role', 'State', 'Password', 'Media_file']
