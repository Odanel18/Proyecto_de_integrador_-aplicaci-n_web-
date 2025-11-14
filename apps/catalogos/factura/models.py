from django.db import models

# Create your models here.
from apps.catalogos.clientes.models import Clientes
from apps.catalogos.metodoPago.models import MetodoPago
from apps.catalogos.caja.models import Caja

class Facturas(models.Model):
    NumFactura= models.IntegerField(verbose_name='Número de factura')
    Fecha = models.DateTimeField(verbose_name='Fecha')
    ClienteId = models.ForeignKey(Clientes, verbose_name='Clientes', on_delete=models.PROTECT)
    MetodoPagoId = models.ForeignKey(MetodoPago, verbose_name='Metodo de pago', on_delete=models.PROTECT)
    Cajaid = models.ForeignKey(Caja, verbose_name='Caja', on_delete=models.PROTECT)
    Total = models.DecimalField(verbose_name='Total',max_digits=10, decimal_places=2)

class Meta :
    Verbose_name_plural = 'Facturas'

def __str__(self):
        return f"{self.NumFactura} - {self.ClienteId}"
    