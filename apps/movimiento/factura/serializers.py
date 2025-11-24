from rest_framework.serializers import ModelSerializer
from .models import Facturas,DetalleFactura

class FacturaSerializer (ModelSerializer):
    class Meta:
        model = Facturas
        fields= ['NumFactura','Fecha','ClienteId','MetodoPagoId','Cajaid','Total']

class DetalleFacturaSerializer (ModelSerializer):
    class Meta:
        model = DetalleFactura
        fields= ['Cantidad','Subtotal','detalleProductoId','FacturaId']