from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from eventos import views

router = routers.DefaultRouter()
router.register(r'usuarios', views.UserViewSet)
router.register(r'eventos', views.EventViewSet)
router.register(r'actividades', views.ActividadViewSet)
router.register(r'noticia', views.NoticiaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
