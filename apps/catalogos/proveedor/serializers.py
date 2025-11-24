from rest_framework.serializers import ModelSerializer
from .models import Proveedores

class ProveedorSerializer(ModelSerializer):
    class Meta:
        model = Proveedores
        fields= ['Nombre','Telefono',]
     