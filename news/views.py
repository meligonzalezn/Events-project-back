from rest_framework import viewsets
from .models import News
from rest_framework.response import Response
from .serializer import NewsSerializer


# Create your views here.
class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
