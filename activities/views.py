from rest_framework import viewsets
from .serializer import ActivitySerializer
from .models import Activity
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()

    @action(detail=True, methods=['put'])
    def update_activity(this, request, pk):
        try:
            activity = Activity.objects.get(id=pk)
            if('ID_event'in request.data):
                activity.ID_Event = request.data['ID_Event']
            if('Date'in request.data):
                activity.Date = request.data['Date']
            if('Init_hour' in request.data):
                activity.Init_hour = request.data['Init_hour']
            if('Final_hour' in request.data):
                activity.Final_hour = request.data['Final_hour']
            if('Space' in request.data):
                activity.Space = request.data['Space'] 
            if('Capacity' in request.data):
                activity.Capacity = request.data['Capacity']
            if('Cost' in request.data):
                activity.Cost = request.data['Cost']
            if('State' in request.data):
                activity.State = request.data['State']      
            if('Details' in request.data):
                activity.Details = request.data['Details']                             
            if('Title' in request.data):
                activity.Title = request.data['Title']
            activity.save()

            return Response("Activity " + activity.Title + " updated", status=status.HTTP_200_OK)
        except:
            return Response("Error", status.HTTP_500_INTERNAL_SERVER_ERROR)