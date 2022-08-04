from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'ID_User', 'ID_Event',
                  'ID_Activity', 'Date', 'Value', 'pay_method']
