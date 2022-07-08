from rest_framework import viewsets
from .serializer import BadgeSerializer
from .models import Badge


class BadgeViewSet(viewsets.ModelViewSet):
    model = Badge
    serializer_class = BadgeSerializer
    queryset = Badge.objects.all()
