from rest_framework.serializers import ModelSerializer
from .models import Compras,DetalleCompra,ComprasCredito

class CompraSerializer (ModelSerializer):
    class Meta:
        model= Compras
        fields= ['Fecha','ProveedoresId','NumCompra','Total']

class DetalleCompraSerializer (ModelSerializer):
    class Meta:
        model = DetalleCompra
        fields= ['Cantidad','detallProductoId','CompraId','PrecioUnitario','Subtotal']

class CompraCreditoSerialezer (ModelSerializer):
    class Meta:
        model=ComprasCredito
        fields=['ProveedoresId','CompraId','FechaInicioCredito','montoTotalCredito','saldoPendiente','FechaLimiteCredito']
