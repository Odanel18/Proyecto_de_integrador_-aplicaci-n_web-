from rest_framework.serializers import ModelSerializer
from .models import Caja

class CajaSerializer(ModelSerializer):
    class Meta:
        model = Caja
        fields= '__all__'
       # fields = ['facturaid', 'monto','cajaid','Fecha_Abono']
                  