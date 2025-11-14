from django.db import models
from apps.catalogos.proveedor.models import Proveedores
from apps.catalogos.metodoPago.models import MetodoPago

# Create your models here.

class Compras (models.Model):
    Fecha= models.DateTimeField()
    MetodoPagoId= models.ForeignKey(MetodoPago,verbose_name='Metodo de pago',on_delete=models.PROTECT)
    ProveedoresId= models.ForeignKey(Proveedores,verbose_name='Proveedor',on_delete=models.PROTECT)
    NumCompra= models.IntegerField(verbose_name='Número de compra')
    Total = models.IntegerField(verbose_name="Total de la compra")
class meta:
    verbose_name_plural='Compras'

def __str__ (self):
    return f"{self.NumCompra} - {self.ProveedoresId}" 

   
