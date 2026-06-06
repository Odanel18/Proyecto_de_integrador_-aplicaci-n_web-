from rest_framework.serializers import ModelSerializer
from .models import TipoMovimientoCaja

class TipoMovimientoCajaSerializer (ModelSerializer):
    class Meta :
        model= TipoMovimientoCaja
        fields=['Tipo']