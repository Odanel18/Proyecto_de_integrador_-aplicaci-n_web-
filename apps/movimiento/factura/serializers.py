from rest_framework.serializers import ModelSerializer,CharField,DateTimeField,JSONField
from .models import Facturas,DetalleFactura,FacturasCredito

class DetalleFacturaSerializer (ModelSerializer):
    producto_nombre = CharField(source='loteId.DetalleCompraId,detallProductoId.producto.Nombre', read_only=True)
    #factura_nombre = CharField(source='FacturaId.NumFactura',read_noly=True)

    class Meta:
        model = DetalleFactura
        fields= ['Cantidad','loteId','producto_nombre',]


class FacturaSerializer (ModelSerializer):
    cliente_nombre = CharField(source='ClienteId.Nombres', read_only=True)
    cliente_cedula = CharField(source='ClienteId.NumCedula', read_only=True)
    condicion_nombre= CharField(source="condicionId.descripcion", read_only=True)
    #estadoCuenta_nommbre= CharField(source='estadoCuentaId.descripcion', read_only=True )
    fecha_formateada= DateTimeField(source='Fecha',format='%d/%m/%Y %I:%M:%S %p',read_only=True)
    #facturaId = CharField(source='id', read_only=True)

    #detalles= DetalleFacturaSerializer(many=True)
    detalles= JSONField(write_only=True, required=False)

    class Meta:
        model = Facturas
        fields= ['NumFactura','fecha_formateada',
                 'ClienteId','condicionId'
                 ,'cliente_nombre','cliente_cedula',
                 'condicion_nombre','detalles',]
        #read_only_fields = ['id', 'Total', 'fecha_formateada']


class FacturaCreditoSerializer (ModelSerializer):
    class Meta:
        model= FacturasCredito
        fields= ['FacturaId','FechaInicioCredito','montoTotalCredito','saldoPendiente','FechaLimiteCredito']
        