from rest_framework import viewsets
from .models import Consulta, Especialista
from .serializers import ConsultaSerializer, EspecialistaSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import viewsets


class ConsultaViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['especialista', 'data']


    def perform_create(self, serializer):
        serializer.save(paciente=self.request.user)


class EspecialistaViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Especialista.objects.all()
    serializer_class = EspecialistaSerializer

