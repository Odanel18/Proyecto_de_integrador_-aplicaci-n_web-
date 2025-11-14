from django.db import models

from apps.catalogos.marca.models import Marcas
from apps.catalogos.moto.models import Motos
from apps.catalogos.categoria.models import Categorias
# Create your models here.
class Productos (models.Model):
    Codigo = models.CharField (verbose_name='Código',max_length=30)
    Nombre= models.CharField (verbose_name='Nombre',max_length=50)
    MarcaId= models.ForeignKey(Marcas,verbose_name='Marca',on_delete=models.PROTECT)
    MotoId= models.ForeignKey(Motos,verbose_name='Moto',on_delete=models.PROTECT)
    CategoriaId = models.ForeignKey(Categorias,verbose_name='Categoria',on_delete=models.PROTECT)
    Stock= models.IntegerField(verbose_name='Stock')
    PrecioVenta=models.DecimalField(verbose_name='Precio de venta',max_digits=10,decimal_places=2)

class meta:
    verbose_Plural="Productos"

def __str__(self):
    return f"{self.Codigo} - {self.Nombre},"