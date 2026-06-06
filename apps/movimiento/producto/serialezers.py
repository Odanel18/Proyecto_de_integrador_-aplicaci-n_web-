from rest_framework.serializers import ModelSerializer
from .models import Productos,DetalleProductos,Registro_Producto

class ProductoSerializer (ModelSerializer):
    class Meta:
        model = Productos
        fields = ['Codigo','Nombre','CategoriaId']

class DetalleProductoSerializer (ModelSerializer):
    class Meta:
        model = DetalleProductos
        fields = ['producto','MarcaId','MotoId','size']

class Registro_ProductoSerialezer(ModelSerializer):
 class Meta:
    model=Registro_Producto
    fields= ['Cantidad','precioCompra','PrecioVenta','FechaRegistro','detalleProductoId']
