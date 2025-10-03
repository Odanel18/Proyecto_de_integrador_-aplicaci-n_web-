from django.db import models
from apps.catalogos.tipo.models import Tipo
# Create your models here.
class Marca (models.Model):
    nombre=models.CharField (verbose_name='Nombre', max_length=50)
    tipoId = models.ForeignKey(Tipo,verbose_name='Tipo', on_delete=models.PROTECT)

class meta:
    verbose_name_plural='Marca'

def __str__ (self):
    return f"{self.nombre}"