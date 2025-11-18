from rest_framework.serializers import ModelSerializer
from .models import Compras,DetalleCompra

class CompraSerializer (ModelSerializer):
    class Meta:
        model= Compras
        fiels= ['Fecha','MetodoPagoId','ProveedoresId','NumCompra','Total']

class DetalleCompraSerializer (ModelSerializer):
    class Meta:
        model = DetalleCompra
        fiels= ['Cantidad','ProductoId','CompraId','PrecioUnitario','Subtotal']
