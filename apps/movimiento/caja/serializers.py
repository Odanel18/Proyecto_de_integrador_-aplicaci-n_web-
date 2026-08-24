from rest_framework.serializers import ModelSerializer,CharField,DateTimeField
from .models import TurnoCaja,MovimientoCaja, Caja

class CajaSerializer(ModelSerializer):
    class Meta:
        model = Caja
        fields = ['id','NumCaja']
class TurnoCajaSerializer(ModelSerializer):
    Empleado_nombre= CharField(source='EmpleadoId.Nombres', read_only=True)
    fecha_incio_formateada= DateTimeField(source='FechaApertura', format='%d/%m/%Y %I:%M:%S %p', read_only= True)
    fecha_cierre_formateada= DateTimeField(source='FechaCierre', format='%d/%m/%Y %I:%M:%S %p', read_only= True)
    class Meta:
        model = TurnoCaja
       # fields= '__all__'
        fields = ['id','SaldoInicial','Egresos','SaldoFinal','FechaApertura','fecha_incio_formateada','FechaCierre','fecha_cierre_formateada','NumCaja','EmpleadoId','Empleado_nombre','Din_efectivo','Din_digital']

class MovimientoCajaSerialiezer(ModelSerializer):
    class Meta:
        model=MovimientoCaja
        fields=['id','turnoCajaId','fecha','tipoMovimientoCajaId','monto','facturaid','compraid','descripcion']

