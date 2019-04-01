from rest_framework import viewsets
from hifuzion.contabilidade.serializers import ClienteSerializer, PlanoContaSerializer
from hifuzion.contabilidade.models import Cliente, PlanoConta


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class PlanoContaViewSet(viewsets.ModelViewSet):
    queryset = PlanoConta.objects.all().order_by('nome')
    serializer_class = PlanoContaSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
