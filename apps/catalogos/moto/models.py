from django.db import models
from apps.catalogos.marca.models import Marca
# Create your models here.
class Moto (models.Model):
    modelo = models.CharField(verbose_name='Modelos',max_length=60)
    año = models.DateField (verbose_name='Año')
    marcaId= models.ForeignKey (Marca,verbose_name='Macar',on_delete=models.PROTECT)

class meta :
    verbose_name_plural='Motos'

def __str__ (self):
    return f"{self.modelo}"