from django.urls import path, include
from rest_framework import routers
from .views import PaymentViewSet

router = routers.DefaultRouter()
router.register(r'', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls))
]
