from distutils.log import debug
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from events import views
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

router = routers.DefaultRouter()
router.register(r'User', views.UserViewSet)
router.register(r'Events', views.EventViewSet)
router.register(r'Activity', views.ActivityViewSet)
router.register(r'News', views.NewsViewSet)

urlpatterns = [
    path('api_schema/', get_schema_view(
        title='API Schema',
        description='Guide for the REST API'
    ), name='api_schema'),
    path('docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'api_schema'}
        ), name='swagger-ui'),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
