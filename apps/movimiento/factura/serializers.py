from rest_framework.serializers import ModelSerializer,CharField,DateTimeField
from .models import Facturas,DetalleFactura,FacturasCredito

class FacturaSerializer (ModelSerializer):
    cliente_nombre = CharField(source='ClienteId.Nombres', read_only=True)
    condicion_nombre= CharField(source="condicionId.descripcion", read_only=True)
    estadoCuenta_nommbre= CharField(source='estadoCuentaId.descripcion', read_only=True )
    fecha_formateada= DateTimeField(source='Fecha',format='%d/%m/%Y %I:%M:%S %p',read_only=True)

    ##detalles= DetalleFacturaSerializer(many=True)

    class Meta:
        model = Facturas
        fields= ['NumFactura','Fecha','fecha_formateada','ClienteId','Total','condicionId','estadoCuentaId','cliente_nombre','condicion_nombre','estadoCuenta_nommbre','detalles']
        #Exception= ['id']

class DetalleFacturaSerializer (ModelSerializer):
    producto_nombre = CharField(source='detalleProductoId.producto', read_only=True)
    #factura_nombre = CharField(source='FacturaId.NumFactura',read_noly=True)

    class Meta:
        model = DetalleFactura
        fields= ['Cantidad','Subtotal','detalleProductoId','producto_nombre','FacturaId']

class FacturaCreditoSerializer (ModelSerializer):
    class Meta:
        model= FacturasCredito
        fields= ['ClienteId','FacturaId','FechaInicioCredito','montoTotalCredito','saldoPendiente','FechaLimiteCredito']
        