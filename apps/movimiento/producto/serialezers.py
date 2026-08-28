from rest_framework.serializers import ModelSerializer,CharField
from .models import Productos,DetalleProductos,RegistroProducto
from rest_framework import serializers

class ProductoSerializer (ModelSerializer):

    categoria_nombre = CharField(source='CategoriaId.Nombre', read_only=True)

    class Meta:
        model = Productos
        fields = ['id', 'Nombre','CategoriaId', 'categoria_nombre']

        extra_kwargs = {'CategoriaId': {'write_only': True}}

class DetalleProductoSerializer (ModelSerializer):
    

    producto_nombre = CharField(source='producto.Nombre', read_only=True)
    marca_nombre = CharField(source='MarcaId.Nombre', read_only=True)
    moto_modelo = serializers.SerializerMethodField(read_only=True)
    color_nombre = CharField(source='colorId.Color', read_only=True)

    class Meta:
        model = DetalleProductos
        fields = ['id',
                  'producto', 
                  'producto_nombre', 
                  'MarcaId', 
                  'marca_nombre', 
                  'MotoId', 
                  'moto_modelo', 
                  'size', 
                  'ColorId', 
                  'color_nombre', 
                  'Codigo'
                  ]

        extra_kwargs = {'producto': {'write_only': True}, 'MarcaId': {'write_only': True}, 'MotoId': {'write_only': True}, 'ColorId': {'write_only': True}}

    def get_moto_modelo(self, obj):
       if obj.MotoId:
            moto_modelo = obj.MotoId
            marca = moto_modelo.MarcaId.Nombre
            modelo = moto_modelo.Modelo
       
            return f"{marca} - {modelo}"

class Registro_ProductoSerializer(ModelSerializer):

    detalle_producto = serializers.SerializerMethodField(read_only=True)
 
    class Meta:
        model=RegistroProducto
        fields= ['id', 
                 'Cantidad', 
                 'precioCosto', 
                 'PrecioVenta', 
                 'FechaRegistro', 
                 'DetalleCompraId', 
                 'detalle_producto']

        extra_kwargs = {'DetalleCompraId': {'write_only': True}}

        read_only_fields = ['FechaRegistro']

    def get_detalle_producto(self, obj):
        if obj.DetalleCompraId:
            detalle_producto = obj.DetalleCompraId.DetalleProductoId
            producto = detalle_producto.producto.Nombre
            marca = detalle_producto.MarcaId.Nombre
            moto = detalle_producto.MotoId.Modelo

            return f"{producto} - {moto} - {marca}"