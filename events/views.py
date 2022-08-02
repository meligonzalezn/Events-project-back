from urllib.request import Request
from rest_framework import viewsets
from .serializer import EventSerializer
from .models import Event
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status




class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


    @action(detail=True, methods=['put'])
    def update_event(this, request, pk):
        try:
            event = Event.objects.get(id=pk)
            if('Title' in request.data):
                event.Title = request.data['Title']
            if('Details' in request.data):
                event.Description = request.data['Details']
            if('Space' in request.data):
                event.Summary = request.data['Space']
            if('State' in request.data):
                event.State = request.data['State']
            if('Cost' in request.data):
                event.State = request.data['Cost']
            if('Media_file' in request.data):
                event.Media_file = request.data['Media_file']
            if('Start_date' in request.data):
                event.Edition_date = request.data['Start_date']
            if('Finish_date' in request.data):
                event.Edition_date = request.data['Finish_date']
            event.save()

            return Response("Event " + event.Title + " updated", status=status.HTTP_200_OK)
        except:
            return Response("Error", status.HTTP_500_INTERNAL_SERVER_ERROR)
    










