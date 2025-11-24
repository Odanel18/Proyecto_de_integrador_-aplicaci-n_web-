from rest_framework.serializers import ModelSerializer
from .models import Compras,DetalleCompra

class CompraSerializer (ModelSerializer):
    class Meta:
        model= Compras
        fields= ['Fecha','MetodoPagoId','ProveedoresId','NumCompra','Total']

class DetalleCompraSerializer (ModelSerializer):
    class Meta:
        model = DetalleCompra
        fields= ['Cantidad','detallProductoId','CompraId','PrecioUnitario','Subtotal']

