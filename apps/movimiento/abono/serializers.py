from rest_framework.serializers import ModelSerializer
from .models import Abonos

class AbonoSerializer(ModelSerializer):
    class Meta:
        model = Abonos
        fields= '__all__'
       # fields = ['facturaid', 'monto','cajaid','Fecha_Abono']
                  