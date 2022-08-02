from django.urls import path, include
from rest_framework import routers
from .views import EventViewSet, PaymentViewSet

router = routers.DefaultRouter()
router.register(r'', EventViewSet)
router.register(r'Payment', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls))
] 
