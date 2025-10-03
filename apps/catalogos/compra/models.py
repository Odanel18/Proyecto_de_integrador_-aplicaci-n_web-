from django.db import models
from apps.catalogos.proveedor.models import Proveedor
from apps.catalogos.metodoPago.models import Metodo_Pago

# Create your models here.

class Compra (models.Model):
    proveedorid= models.ForeignKey(Proveedor,verbose_name='Proveedor',on_delete=models.PROTECT)
    Num_compra= models.IntegerField(verbose_name='Número de compra')
    metodo_Pagoid= models.ForeignKey(Metodo_Pago,verbose_name='Metodo de pago',on_delete=models.PROTECT)
    Fecha= models.DateField()

class meta:
    verbose_name_plural='Compras'

def __str__ (self):
    return f"{self.Num_compra} - {self.proveedorid}"    
