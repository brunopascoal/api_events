from django.urls import path, include
from rest_framework import routers
from .views import EventoViewSet

router = routers.DefaultRouter()
router.register(r'eventos', EventoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
