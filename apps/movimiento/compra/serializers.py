from rest_framework.serializers import ModelSerializer, SerializerMethodField,JSONField
from .models import Compras,DetalleCompra,ComprasCredito


class CompraSerializer(ModelSerializer):
    # Devuelve el nombre del proveedor en lugar del ID
    proveedor_nombre = SerializerMethodField()
    # Devuelve la descripción de la condición de pago en lugar del ID
    condicion_descripcion = SerializerMethodField()
    # Devuelve la descripción del estado de cuenta en lugar del ID
    #estado_cuenta_descripcion = SerializerMethodField()

    detallesCompra = JSONField(write_only=True, required=False)  # Campo para recibir los detalles de la compra

    class Meta:
        model = Compras
        fields = [
            'id',
            'NumCompra',
            'Fecha',
            'Total',
            'ProveedoresId',
            'proveedor_nombre',
            'condicionId',
            'condicion_descripcion',
            #'estado_cuenta_descripcion',
            'detallesCompra'
        ]

    def get_proveedor_nombre(self, obj):
        # Retorna el nombre del proveedor relacionado
        if obj.ProveedoresId:
            return obj.ProveedoresId.Nombre
        return '-'

    def get_condicion_descripcion(self, obj):
        # Retorna la descripción de la condición de pago relacionada
        if obj.condicionId:
            return obj.condicionId.descripcion
        return '-'

    #def get_estado_cuenta_descripcion(self, obj):
        # Retorna la descripción del estado de cuenta relacionado
        if obj.estadoCuentaId:
            # Ajusta el nombre del campo según tu modelo EstadoCuenta
            return str(obj.estadoCuentaId)
        return '-'

class DetalleCompraSerializer (ModelSerializer):
    class Meta:
        model = DetalleCompra
        fields= ['id','Cantidad','detallProductoId',
                 'CompraId','PrecioUnitario','Subtotal']

class CompraCreditoSerialezer (ModelSerializer):
    class Meta:
        model=ComprasCredito
        fields=['id','CompraId','FechaInicioCredito',
                'montoTotalCredito','saldoPendiente',
                'FechaLimiteCredito','estadoCuentaId']
