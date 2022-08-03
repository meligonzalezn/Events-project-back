from rest_framework import viewsets
from .serializer import PaymentSerializer
from .models import Payment


class PaymentViewSet(viewsets.ModelViewSet):

    model = Payment
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
