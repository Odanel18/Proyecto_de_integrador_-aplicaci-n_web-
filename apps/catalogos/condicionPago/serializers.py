from rest_framework.serializers import ModelSerializer
from .models import CondicionPago

class CondicionPagoSerializer (ModelSerializer):
    class Meta:
        model= CondicionPago
        fields= ['descripcion']
