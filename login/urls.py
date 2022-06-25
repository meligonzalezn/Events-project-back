from django.urls import path, include
from rest_framework import routers
from .views import LoginViewSet

# router = routers.DefaultRouter()
# router.register(r'', LoginViewSet)


urlpatterns = [
    path('perms',
         LoginViewSet.as_view({
             'post': 'has_access'
         })),
    path('',
         LoginViewSet.as_view({
             'get': 'get',
             'post': 'post',
             'delete': 'delete'
         })
        ),
]
