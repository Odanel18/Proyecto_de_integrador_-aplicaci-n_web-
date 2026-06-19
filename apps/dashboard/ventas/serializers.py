from .models import dimCliente,dimCondicionPago, dimEmpleado, dimMetodoPago, dimProducto, dimTiempo, FactVenta
from rest_framework import serializers
from rest_framework.serializers import CharField

class dimClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=dimCliente
        fields='__all__'

class dimCondicionPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model=dimCondicionPago
        fields='__all__'

class dimEmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model=dimEmpleado
        fields='__all__'

class dimMetodoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model=dimMetodoPago
        fields='__all__'

class dimProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model=dimProducto
        fields='__all__'

class dimTiempoSerializer(serializers.ModelSerializer):
    class Meta:
        model=dimTiempo
        fields='__all__'

class FactVentaSerializer(serializers.ModelSerializer):
    empleado_nombre = CharField(source='id_Empleado.Nombres', read_only=True)
    cliente_nombre = CharField(source='id_Cliente.Nombres', read_only=True)
    metodo_pago_tipo = CharField(source='id_MetodoPago.Tipo', read_only=True)
    condicion_pago_descripcion = CharField(source='id_CondicionPago.Descripcion', read_only=True)
    producto_nombre = CharField(source='id_Producto.Nombre', read_only=True)
    #tiempo_dia = CharField(source='id_Tiempo.Dia'+ 'id_Tiempo.Mes' + 'id_Tiempo.Año', read_only=True)
    tiempo_año = CharField(source='id_Tiempo.Año', read_only=True)

    class Meta:
        model=FactVenta
        fields= ['id_Venta','id_Empleado','empleado_nombre','id_Cliente','cliente_nombre','id_MetodoPago','metodo_pago_tipo'
                 ,'id_CondicionPago','condicion_pago_descripcion',
                 'id_Producto','producto_nombre','id_Tiempo','tiempo_año','Cantidad','Subtotal',
                 'PrecioUnitario','NumFactura']

