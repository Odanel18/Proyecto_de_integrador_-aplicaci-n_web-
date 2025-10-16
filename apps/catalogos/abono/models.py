from django.db import models
from apps.catalogos.factura.models import factura
from apps.catalogos.caja.models import Caja
# Create your models here.

class Abono (models.Model):
    facturaid = models.ForeignKey(factura,verbose_name="factura",on_delete=models.PROTECT)
    monto= models.DecimalField(verbose_name='Montos', max_digits=10,decimal_places=2)
    cajaid = models.IntegerField(verbose_name='Caja')
    Fecha_Abono= models.DateField (verbose_name='Fecha de abono')

class Meta:
    verbose_name_plural='Abonos'

def __str__ (self):
    return f"{self.facturaid}"