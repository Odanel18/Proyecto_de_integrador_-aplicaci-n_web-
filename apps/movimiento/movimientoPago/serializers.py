from rest_framework.serializers import ModelSerializer, CharField
from rest_framework import serializers
from .models import MovimientoPago

class MovimientoPagoSerializer(ModelSerializer):

    metodoPago_nombre = serializers.CharField(source='metodoPagoId.Tipo', read_only=True)
    movimientocaja_nombre= serializers.SerializerMethodField()
    
    class Meta:
        model = MovimientoPago
        fields = ['id', 'monto', 'metodoPagoId', 'MovimientoCajaId', 'metodoPago_nombre', 'movimientocaja_nombre']

        extra_kwargs = {'metodoPagoId': {'write_only': True}, 'MovimientoCajaId': {'write_only': True}}

    def get_movimientocaja_nombre(self, obj):
        if obj.MovimientoCajaId:
            movimientocaja_nombre = obj.MovimientoCajaId
            descripcion = movimientocaja_nombre.descripcion
            tipo_movimiento = movimientocaja_nombre.tipoMovimientoCajaId.Tipo
            return f"{descripcion} - {tipo_movimiento}"