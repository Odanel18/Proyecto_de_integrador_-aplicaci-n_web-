from django.db import models
from apps.catalogos.factura.models import Facturas
from apps.catalogos.producto.models import Productos

# Create your models here.
class DetalleFactura (models.Model):
    Cantidad = models.IntegerField(verbose_name="Cantidad")
    Subtotal= models.DecimalField (verbose_name='Precio costo',max_digits=7, decimal_places=2)
    ProductoId = models.ForeignKey (Productos,verbose_name='Productos',on_delete=models.PROTECT)
    FacturaId= models.ForeignKey (Facturas,verbose_name="Factura",on_delete=models.PROTECT)

class Meta :
    verbose_plural="Detalles factura"
def __str__ (self):
    return f"{self.FacturaId}"