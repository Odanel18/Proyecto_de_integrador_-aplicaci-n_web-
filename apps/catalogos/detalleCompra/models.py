from django.db import models

from apps.catalogos.compra.models import Compras
from apps.catalogos.producto.models import Productos

# Create your models here.
class DetalleCompra (models.Model):
    Cantidad = models.IntegerField(verbose_name="Cantidad")
    ProductoId = models.ForeignKey (Productos,verbose_name='Productos',on_delete=models.PROTECT)
    CompraId= models.ForeignKey (Compras,verbose_name="Compra",on_delete=models.PROTECT)
    PrecioUnitario = models.DecimalField (verbose_name='Precio costo',max_digits=7, decimal_places=2)
    Subtotal= models.DecimalField (verbose_name='Subtotal', max_digits=7, decimal_places=2)

class meta:
    verbose_name_plural='Detalles de compra'

def __str__ (self):
    return f"{self.CompraId}"