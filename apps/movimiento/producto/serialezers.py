from rest_framework.serializers import ModelSerializer
from .models import Productos,DetalleProductos

class ProductoSerializer (ModelSerializer):
    class Meta:
        model = Productos
        fields = ['Codigo','Nombre','CategoriaId']

class DetalleProductoSerializer (ModelSerializer):
    class Meta:
        model = DetalleProductos
        fields = ['producto','MarcaId','MotoId','PrecioVenta','precioCompra','Stock','size']