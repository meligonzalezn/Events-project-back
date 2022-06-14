from rest_framework import viewsets
from .serializer import ActivitySerializer
from .models import Activity

# Create your views here.
class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()