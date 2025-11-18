from rest_framework.serializers import ModelSerializer
from .models import Categorias

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categorias
        fields= ['Nombre']
       # fields = ['facturaid', 'monto','cajaid','Fecha_Abono']
                  