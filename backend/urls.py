from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from events import views

router = routers.DefaultRouter()
router.register(r'User', views.UserViewSet)
router.register(r'Events', views.EventViewSet)
router.register(r'Activity', views.ActivityViewSet)
router.register(r'News', views.NewsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
