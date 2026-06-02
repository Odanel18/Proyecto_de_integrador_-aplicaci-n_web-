from rest_framework.serializers import ModelSerializer
from .models import Facturas,DetalleFactura,FacturasCredito

class FacturaSerializer (ModelSerializer):
    class Meta:
        model = Facturas
        fields= ['NumFactura','Fecha','ClienteId','Total','condicionId','estadoCuentaId']
        #Exception= ['id']

class DetalleFacturaSerializer (ModelSerializer):
    class Meta:
        model = DetalleFactura
        fields= ['Cantidad','Subtotal','detalleProductoId','FacturaId']

class FacturaCreditoSerializer (ModelSerializer):
    class Meta:
        model= FacturasCredito
        fields= ['ClienteId','FacturaId','FechaInicioCredito','montoTotalCredito','saldoPendiente','FechaLimiteCredito']
        