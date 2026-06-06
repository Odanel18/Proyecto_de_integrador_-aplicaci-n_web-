from rest_framework.serializers import ModelSerializer
from .models import Caja,MovimientoCaja

class CajaSerializer(ModelSerializer):
    class Meta:
        model = Caja
       # fields= '__all__'
        fields = ['SaldoInicial','Egresos','SaldoFinal','FechaApertura','FechaCierre','NumCaja','EmpleadoId','Din_efectivo','Din_digital','abierta']

class MovimientoCajaSerialiezer(ModelSerializer):
    class Meta:
        model=MovimientoCaja
        fields=['cajaId','fecha','tipoMovimientoCajaId','monto','facturaid','compraid','descripcion']

