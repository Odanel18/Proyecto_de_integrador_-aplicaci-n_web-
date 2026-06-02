from rest_framework.serializers import ModelSerializer
from .models import OrigenSaldo

class OrigenSaldoSerializer (ModelSerializer):
    class Meta:
        model= OrigenSaldo
        fields= ['descripcion']
