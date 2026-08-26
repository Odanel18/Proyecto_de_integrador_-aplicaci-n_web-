from rest_framework.serializers import ModelSerializer,CharField
from .models import Productos,DetalleProductos,RegistroProducto

class ProductoSerializer (ModelSerializer):
    class Meta:
        model = Productos
        fields = ['id','Codigo','Nombre','CategoriaId']

class DetalleProductoSerializer (ModelSerializer):
    

    producto_nombre = CharField(source='producto.Nombre', read_only=True)
    marca_nombre = CharField(source='MarcaId.Nombre', read_only=True)
    moto_modelo = CharField(source='MotoId.MarcaId.Nombre', read_only=True)
    color_nombre = CharField(source='colorId.Color', read_only=True)

    class Meta:
        model = DetalleProductos
        fields = ['id','producto','producto_nombre','MarcaId','marca_nombre','MotoId','moto_modelo','size','ColorId','color_nombre']

class Registro_ProductoSerializer(ModelSerializer):
 #nombreProducto = CharField(source = 'DetalleCompraId.detalleProductoId.producto.Nombre', read_only=True)
 #DetalleCompraIdProducto = CharField(source='DetalleCompraId.detalleProductoId.producto.Nombre', read_only=True)
 nombreMarca = CharField(source = 'detalleProductoId.MarcaId.Nombre', read_only=True)
 nombreMoto = CharField(source = 'detalleProductoId.MotoId.MarcaId.Nombre', read_only=True)
 
 
 class Meta:
    model=RegistroProducto
    fields= ['id','Cantidad','precioCompra','PrecioVenta','FechaRegistro','DetalleCompraId','nombreMarca','nombreMoto']
