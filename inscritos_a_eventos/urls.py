from django.urls import path, include
from rest_framework import routers
from .views import EnrollViewSet


urlpatterns = [
    path('',
         EnrollViewSet.as_view({
             'get': 'get_participants',
             'post': 'enroll_user2event',
         })
        ),
]
