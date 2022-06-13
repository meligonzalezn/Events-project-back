from django.urls import path, include
from rest_framework import routers
from .views import ActivityViewSet
router = routers.DefaultRouter()
router.register(r'', ActivityViewSet)

urlpatterns = [
  path('', include(router.urls))
]
