from datetime import datetime
from sqlite3 import Date
from urllib.request import Request
from rest_framework import viewsets
from .serializer import EventSerializer, PaymentSerializer
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

    @action(detail=True, methods=['get'])
    def get_participants(self, request: Request, event_id: int):
        """
        Get all event participants using event_id
        """
        try:
            query = Payment.objects.all().get(ID_Event=event_id)
            serializer = self.serializer_class(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Payment.DoesNotExist:
            return HTTP_ERRORS.OBJECT_NOT_FOUND
        except:
            return HTTP_ERRORS.INTERNAL_ERROR
    
    @action(detail=True, methods=['post'])
    def add_participants(self, request, event_id: int):
        try:
            new_event = {
                'ID_User': cache.get('member_id'),
                'ID_Event': event_id,
                'Date': datetime.now(),
                'Value': request.data['value'],
                'pay_method': request.data['pay_method']
            }
            
            query = Payment.objects.all()
            serializer = PaymentSerializer.create(data=new_event)
            return HTTP_ERRORS.AC
        except:
            return HTTP_ERRORS.INTERNAL_ERROR
            
        
        


class EventViewSet(viewsets.ModelViewSet):
    model = Event
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    @action(detail=True, methods=['get'], url_path='bring')
    def traer(self, request, format=None):

        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("monda", status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['put'], url_path='update')
    def actualizar(this, request, pk):
        # try:
        event = Event.objects.get(id=pk)

        if('Title' in request.data):
            event.Title = request.data['Title']

        event.save()

        return Response("User " + event.Title + " updated", status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], url_path='crea')
    def crea(this, request, pk):
        # try:
        user = User.objects.get(id=pk)

        if('Name' in request.data):
            user.Name = request.data['Name']
        if('State' in request.data):
            user.State = request.data['State']
        if('Role' in request.data):
            user.Role = request.data['Role']
        if('Email' in request.data):
            user.Email = request.data['Email']
        if('Phone' in request.data):
            user.Phone = request.data['Phone']
        if('Password' in request.data):
            user.Password = request.data['Password']
        user.save()

        return Response("User " + user.Name + " updated", status=status.HTTP_200_OK)
    # @action(detail=True, methods=['get'], url_path='watch')
    # ##
    # def get_events(request: Request):
    #     try:
    #         query = Event.objects.all()
    #         serializer: EventSerializer = self.serializer_class(query, many=False)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     except:
    #         return Response("Events don't exist", status=status.HTTP_400_BAD_REQUEST)
