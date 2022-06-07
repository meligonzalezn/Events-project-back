from distutils.log import debug
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from events import views
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'User', views.UserViewSet)
router.register(r'Events', views.EventViewSet)
router.register(r'Activity', views.ActivityViewSet)
router.register(r'News', views.NewsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
