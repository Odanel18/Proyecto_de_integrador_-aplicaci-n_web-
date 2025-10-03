from django.db import models

from apps.catalogos.compra.models import Compra
from apps.catalogos.producto.models import Producto

# Create your models here.
class DetalleCompra (models.Model):
    compraid= models.ForeignKey (Compra,verbose_name="Compra",on_delete=models.PROTECT)
    productoid = models.ForeignKey (Producto,verbose_name='Productos',on_delete=models.PROTECT)
    cantidad = models.IntegerField(verbose_name="Cantidad")
    Precio_costo = models.DecimalField (verbose_name='Precio costo',max_digits=7, decimal_places=2)
def __str__ (self):
    return f"{self.compraid}"