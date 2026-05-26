#
from rest_framework.serializers import ModelSerializer
from .models import MovimientoPago

class MovimientoPagoSerializer(ModelSerializer):
    class Meta:
        model = MovimientoPago

        fields= ['monto','fecha','metodoPagoId','facturaId','facturaCreditoId','tipoMovimientoCajaId','origenSaldoId','compraId','compraCreditoId']