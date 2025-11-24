from rest_framework.serializers import ModelSerializer
from .models import Caja

class CajaSerializer(ModelSerializer):
    class Meta:
        model = Caja
       # fields= '__all__'
        fields = ['SaldoInicial', 'Ingresos','Egresos','SaldoFinal','Fecha','NumCaja','EmpleadoId','Dinero']