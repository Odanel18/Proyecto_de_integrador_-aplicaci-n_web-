from django.db import models

from apps.catalogos.marca.models import Marca
from apps.catalogos.moto.models import Moto
from apps.catalogos.categoria.models import Categoria
# Create your models here.
class Producto (models.Model):
    codigo = models.CharField (verbose_name='Código',max_length=30)
    nombre= models.CharField (verbose_name='Nombre',max_length=30)
    precio_venta=models.DecimalField(verbose_name='Precio de venta',max_digits=10,decimal_places=2)
    marcaId= models.ForeignKey(Marca,verbose_name='Marca',on_delete=models.PROTECT)
    stock= models.IntegerField(verbose_name='Stock')
    motoid= models.ForeignKey(Moto,verbose_name='Moto',on_delete=models.PROTECT)
    categoriaId = models.ForeignKey(Categoria,verbose_name='Categoria',on_delete=models.PROTECT)