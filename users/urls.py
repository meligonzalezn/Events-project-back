from distutils.log import debug
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from users.views import UserViewSet
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
router = routers.DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
  path('', include(router.urls))
]
