from rest_framework.serializers import ModelSerializer
from .models import Clientes

class ClienteSerializer (ModelSerializer):
    class Meta:
        model= Clientes
        fields= ['id','Nombres','Apellidos','NumCedula','NumTeléfono']
