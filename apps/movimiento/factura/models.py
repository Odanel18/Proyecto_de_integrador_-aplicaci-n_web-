from django.db import models

from apps.catalogos.clientes.models import Clientes
from apps.catalogos.metodoPago.models import MetodoPago
from apps.movimiento.caja.models import Caja
from apps.movimiento.producto.models import Productos

class Facturas(models.Model):
    NumFactura= models.IntegerField(verbose_name='Número de factura')
    Fecha = models.DateTimeField(verbose_name='Fecha')
    ClienteId = models.ForeignKey(Clientes, verbose_name='Clientes', on_delete=models.PROTECT)
    MetodoPagoId = models.ForeignKey(MetodoPago, verbose_name='Metodo de pago', on_delete=models.PROTECT)
    Cajaid = models.ForeignKey(Caja, verbose_name='Caja', on_delete=models.PROTECT)
    Total = models.DecimalField(verbose_name='Total',max_digits=10, decimal_places=2)

    class Meta :
        verbose_name_plural = 'Facturas'

def __str__(self):
        return f"{self.NumFactura} - {self.ClienteId}"
    

# Create your models here.
class DetalleFactura (models.Model):
    Cantidad = models.IntegerField(verbose_name="Cantidad")
    Subtotal= models.DecimalField (verbose_name='Precio costo',max_digits=7, decimal_places=2)
    ProductoId = models.ForeignKey (Productos,verbose_name='Productos',on_delete=models.PROTECT)
    FacturaId= models.ForeignKey (Facturas,verbose_name="Factura",on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural="Detalles de factura"
    def __str__ (self):
        return f"{self.FacturaId}"