from rest_framework.viewsets import ModelViewSet
from .models import Tipo
from .serializers import TipoSerializer

class TipoModelViewSet(ModelViewSet):
    queryset=Tipo.objects.filter(estado=True)
    serializer_class= TipoSerializer