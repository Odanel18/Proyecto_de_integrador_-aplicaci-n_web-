from django.db import models
from apps.catalogos.metodoPago.models import MetodoPago
from apps.movimiento.caja.models import MovimientoCaja

class MovimientoPago(models.Model):
    monto = models.DecimalField (verbose_name='Monto',max_digits=10, decimal_places=2)
    metodoPagoId = models.ForeignKey(MetodoPago, verbose_name='Metodo de pago', on_delete=models.PROTECT)
    MovimientoCajaId = models.ForeignKey(MovimientoCaja, verbose_name='Movimiento de caja', on_delete=models.PROTECT)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Movimientos de pago"

    def __str__ (self):
        return f"Movimiento de pago {self.id}"
