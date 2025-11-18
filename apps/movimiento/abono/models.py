from django.db import models
from apps.movimiento.factura.models import Facturas
from apps.movimiento.caja.models import Caja
from apps.catalogos.metodoPago.models import MetodoPago
            
# Create your models here.

class Abonos (models.Model):
    FechaAbono= models.DateTimeField (verbose_name='Fecha de abono')
    Monto= models.DecimalField(verbose_name='Montos', max_digits=10,decimal_places=2)
    Detalle= models.CharField(verbose_name="Detalle", max_length=100)
    FacturaId = models.ForeignKey(Facturas,verbose_name="factura",on_delete=models.PROTECT)
    CajaId = models.ForeignKey(Caja,verbose_name="Caja", on_delete=models.PROTECT)
    MetodoPagoId = models.ForeignKey(MetodoPago,verbose_name="Metodo de pago", on_delete=models.PROTECT)

    class Meta:
      # verbose_name = 'Abonos'
        #managed = False  # 🔹 Muy importante: Django no crea ni modifica esta tabla
       # app_label = 'apps.catalogos.abono'
        verbose_name_plural = 'Abonos' # 🔹 Nombre exacto de la tabla en SQL Server

    def __str__ (self):
        return f"{self.Monto} - {self.FacturaId}"