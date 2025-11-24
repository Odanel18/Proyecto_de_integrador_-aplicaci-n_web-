from rest_framework.serializers import ModelSerializer
from .models import MetodoPago

class MetodoPagoSerializer (ModelSerializer):
    class Meta:
        model = MetodoPago
        fields=['Tipo']