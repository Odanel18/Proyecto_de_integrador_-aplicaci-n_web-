from django.db import models
from apps.catalogos.factura.models import factura
from apps.catalogos.producto.models import Producto

# Create your models here.
class DetalleFactura (models.Model):
    facturaid= models.ForeignKey (factura,verbose_name="Factura",on_delete=models.PROTECT)
    productoid = models.ForeignKey (Producto,verbose_name='Productos',on_delete=models.PROTECT)
    cantidad = models.IntegerField(verbose_name="Cantidad")
    total= models.DecimalField (verbose_name='Precio costo',max_digits=7, decimal_places=2)
def __str__ (self):
    return f"{self.FacturaId}"