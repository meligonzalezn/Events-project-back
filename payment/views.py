from datetime import datetime
from sqlite3 import Date
from urllib.request import Request
from rest_framework import viewsets
from .serializer import PaymentSerializer
from .models import Payment, User, Event
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from static.http_error_response import HTTP_ERRORS
from django.core.cache import cache

class PaymentViewSet(viewsets.ModelViewSet):
    model = Payment
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    http_method_names = ['get', 'post']
    
    @action(detail=True, methods=['get'], url_path='enroll_user2event')
    def enroll_user2event(self, request: Request, pk: int):
        try:
            userId = cache.get('member_id')
            user = User.objects.get(id=userId)
            event = Event.objects.get(id=pk)
            new_payment = Payment.objects.create(ID_User=user, ID_Event=event, Date=Date.today(), Value=0, pay_method='')
            return HTTP_ERRORS.SuccessfulPetition("enrollment petition finished. Payment_ID" + str(new_payment.id))
        except KeyError:
            return HTTP_ERRORS.KEY_ERROR
        except User.DoesNotExist:
            return HTTP_ERRORS.OBJECT_NOT_FOUND
        except:
            return HTTP_ERRORS.INTERNAL_ERROR

    @action(detail=True, methods=['get'])
    def get_participants(self, request: Request, pk: int):
        """
        Get all event participants using event_id
        """
        try:
            query = Payment.objects.all().get(ID_Event=pk)
            serializer = self.serializer_class(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Payment.DoesNotExist:
            return HTTP_ERRORS.OBJECT_NOT_FOUND
        except:
            return HTTP_ERRORS.INTERNAL_ERROR
    
    @action(detail=True, methods=['post'])
    def add_participants(self, request, pk: int):
        try:
            new_event = {
                'ID_User': cache.get('member_id'),
                'ID_Event': pk,
                'Date': datetime.now(),
                'Value': request.data['value'],
                'pay_method': request.data['pay_method']
            }
            
            query = Payment.objects.all()
            serializer = PaymentSerializer.create(data=new_event)
            return HTTP_ERRORS.AC
        except:
            return HTTP_ERRORS.INTERNAL_ERROR