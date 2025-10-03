from django.db import models

# Create your models here.
from apps.catalogos.clientes.models import Cliente
from apps.catalogos.metodoPago.models import Metodo_Pago
from apps.catalogos.caja.models import Caja

class factura(models.Model):
    num_Factura= models.IntegerField(verbose_name='Número de factura')
    fecha = models.DateTimeField(verbose_name='Fecha')
    clienteId = models.ForeignKey(Cliente, verbose_name='Clientes', on_delete=models.PROTECT)
    Metodo_PagoId = models.ForeignKey(Metodo_Pago, verbose_name='Metodo de pago', on_delete=models.PROTECT)
    cajaid = models.ForeignKey(Caja, verbose_name='Caja', on_delete=models.PROTECT)
    total = models.DecimalField(verbose_name='Total',max_digits=10, decimal_places=2)

class Meta :
    Verbose_name_plural = 'Facturas'

def __str__(self):
        return f"{self.num_Factura} - {self.clienteId}"
    