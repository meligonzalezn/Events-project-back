from django.urls import path, include
from rest_framework import routers
from .views import EnrollViewSet

router = routers.DefaultRouter()
router.register(r'', EnrollViewSet)

urlpatterns = [
    path('', include(router.urls))
]
