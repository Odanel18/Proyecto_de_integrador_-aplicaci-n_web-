from rest_framework.serializers import ModelSerializer, CharField, DateField
from rest_framework import serializers
from .models import Compras, DetalleCompra, ComprasCredito
from apps.movimiento.compra.service.validaciones import validar_compra

class DetalleCompraSerializer(ModelSerializer):

    PrecioVenta = serializers.DecimalField(max_digits=7, decimal_places=2, write_only=True)
    Detalle_Producto = serializers.SerializerMethodField()

    class Meta:
        
        model = DetalleCompra
        fields = [  'id',
                    'Cantidad',
                    'PrecioUnitario',
                    'Subtotal',
                    'CompraId',
                    'DetalleProductoId',
                    'Detalle_Producto',
                    'PrecioVenta'
                   ]
        
        read_only_fields = [
                                'Subtotal',
                            ]

        write_only_fields = [
                                'id',
                                'DetalleProductoId',
                                'CompraId'
                            ]
        
    def get_Detalle_Producto(self, obj):
        if obj.DetalleProductoId:
            detalle_producto = obj.DetalleProductoId
            producto = detalle_producto.producto.Nombre
            marca = detalle_producto.MarcaId.Nombre
            moto = detalle_producto.MotoId.Modelo

            return f"{producto} - {marca} - {moto}"

class CompraSerializer(ModelSerializer):

    Proveedor_nombre = CharField(source='ProveedorId.Nombre', read_only=True)
    CondicionPago_nombre = CharField(source='CondicionPagoId.descripcion', read_only=True)
    Fecha = DateField(required=True, input_formats=['%Y-%m-%d'], format='%Y-%m-%d')
    detalles_Compra = DetalleCompraSerializer(many=True, source='detallesCompra', required=True)
    FechaVencimiento = DateField(required=False, write_only=True, input_formats=['%Y-%m-%d'], format='%Y-%m-%d')

    class Meta:
        
        model = Compras
        fields = [
                    'id',
                    'Fecha',
                    'NumCompra',
                    'Total',
                    'ProveedorId',
                    'CondicionPagoId',
                    'Proveedor_nombre',
                    'CondicionPago_nombre',
                    'detalles_Compra',
                    'FechaVencimiento'
                  ]
        
        read_only_fields = [
                                'Total',
                            ]

        write_only_fields = [
                                'id',
                                'ProveedorId',
                                'CondicionPagoId'
                            ]

    def validate(self, data):
        validar_compra(data)
        return data

class CompraCreditoSerializer(ModelSerializer):

    estado_cuenta_nombre = CharField(source='EstadoCuentaId.descripcion', read_only=True)
    Compra_nombre = serializers.SerializerMethodField()

    class Meta:
        
        model = ComprasCredito
        fields = [
                    'MontoTotal',
                    'SaldoPendiente',
                    'FechaInicio',
                    'FechaVencimiento',
                    'CompraId',
                    'Compra_nombre',
                    'EstadoCuentaId',
                    'estado_cuenta_nombre'
                ]
        
        read_only_fields = [
                                'FechaInicio',
                                'SaldoPendiente',
                                'MontoTotal'
                            ]

        write_only_fields = [
                                'CompraId',
                                'EstadoCuentaId'
                            ]
        
        
    
    def get_Compra_nombre(self, obj):
        if obj.CompraId:
            compra = obj.CompraId
            num_compra = compra.NumCompra
            proveedor_nombre = compra.ProveedorId.Nombre
            return f"Compra {num_compra} - {proveedor_nombre}"