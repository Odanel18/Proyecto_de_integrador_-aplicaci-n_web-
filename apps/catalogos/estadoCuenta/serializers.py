from rest_framework.serializers import ModelSerializer
from .models import EstadoCuenta

class EstadoCuentaSerializer (ModelSerializer):
    class Meta:
        model = EstadoCuenta
        fields=['descripcion']