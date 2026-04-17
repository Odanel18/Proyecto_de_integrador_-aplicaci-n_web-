from django.db import models

from apps.catalogos.metodoPago.models import MetodoPago
from apps.movimiento.factura.models import Facturas
from apps.movimiento.factura.models import FacturasCredito
from apps.catalogos.tipoMovimientoCaja.models import TipoMovimientoCaja
from apps.catalogos.origenSaldo.models import OrigenSaldo
from apps.movimiento.compra.models import Compras
from apps.movimiento.compra.models import ComprasCredito

class MovimientoPago(models.Model):
    monto = models.DecimalField (verbose_name='Monto',max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(verbose_name='Fecha')
    metodoPagoId = models.ForeignKey(MetodoPago, verbose_name='Metodo de pago', on_delete=models.PROTECT)
    facturaId = models.ForeignKey(Facturas, verbose_name='Factura', null=True, blank=True, on_delete=models.PROTECT)
    facturaCreditoId = models.ForeignKey(FacturasCredito, verbose_name='Factura al credito', null=True, blank=True, on_delete=models.PROTECT)
    tipoMovimientoCajaId = models.ForeignKey(TipoMovimientoCaja, verbose_name='Tipo de movimiento', on_delete=models.PROTECT)
    origenSaldoId = models.ForeignKey(OrigenSaldo, verbose_name='Origen del saldo', on_delete=models.PROTECT)
    compraId = models.ForeignKey(Compras, verbose_name='Compra', null=True, blank=True, on_delete=models.PROTECT)
    compraCreditoId= models.ForeignKey(ComprasCredito, verbose_name='Compra al credito', null=True, blank=True, on_delete=models.PROTECT)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Movimientos de pago"

    def __str__ (self):
        return f"Movimiento de pago {self.id}"
