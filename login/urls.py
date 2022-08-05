from django.urls import path, include
from rest_framework import routers
from .views import LoginViewSet

# router = routers.DefaultRouter()
# router.register(r'', LoginViewSet)


urlpatterns = [
    path('',
         LoginViewSet.as_view({
             'post': 'post',
         })
        ),
]
