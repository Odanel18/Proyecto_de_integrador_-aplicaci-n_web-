from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Size (models.Model):
    descripcion= models.CharField(verbose_name='Tamaño', max_length=50)

    class Meta:
        verbose_name_plural= 'Sizes'

    def __str__ (self):
        return f"{self.descripcion}"