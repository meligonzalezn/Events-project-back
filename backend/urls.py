from distutils.log import debug
import os
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from django.views.generic.base import RedirectView

router = routers.DefaultRouter()

urlpatterns = [
    path("User/", include("users.urls")),
    path("Events/", include("events.urls")),
    path("Activity/", include("activities.urls")),
    path("News/", include("news.urls")),
    path("login/", include("login.urls")),
    path("Payment/", include("payment.urls")),
    path("Enroll/", include("enrolled_events.urls")),
    path('api_schema/', get_schema_view(
        title='API Schema',
        description='Guide for the REST API'
    ), name='api_schema'),
    path('docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url': 'api_schema'}
    ), name='swagger-ui'),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
