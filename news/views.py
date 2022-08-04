from rest_framework import viewsets
from .models import News
from rest_framework.response import Response
from .serializer import NewsSerializer
from rest_framework import status
from rest_framework.decorators import action


# Create your views here.
class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()

    @action(detail=True, methods=['put'])
    def update_news(this, request, pk):
        try:
            news = News.objects.get(id=pk)
            if('ID_event'in request.data):
                news.ID_event = request.data['ID_event']
            if('ID_user'in request.data):
                news.ID_user = request.data['ID_user']
            if('Title' in request.data):
                news.Title = request.data['Title']
            if('Description' in request.data):
                news.Description = request.data['Description']
            if('Summary' in request.data):
                news.Summary = request.data['Summary']
            if('State' in request.data):
                news.State = request.data['State']
            if('Media_file' in request.data):
                news.Media_file = request.data['Media_file']
            if('Edition_date' in request.data):
                news.Edition_date = request.data['Edition_date']
            if('Finish_date' in request.data):
                news.Finish_date = request.data['Finish_date']
            news.save()

            return Response("News " + news.Title + " updated", status=status.HTTP_200_OK)
        except:
            return Response("Error", status.HTTP_500_INTERNAL_SERVER_ERROR)