from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConsultaViewSet, EspecialistaViewSet

router = DefaultRouter()
router.register(r'consultas', ConsultaViewSet, basename='consulta')
router.register(r'especialistas', EspecialistaViewSet, basename='especialista')

urlpatterns = [
    path('', include(router.urls)),
]