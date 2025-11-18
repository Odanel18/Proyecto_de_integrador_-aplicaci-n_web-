from django.db import models

# Create your models here.
class Tipo (models.Model):
    TipoMarca=models.CharField(verbose_name='Tipo de marca', max_length=50)

    class Meta:
        verbose_name_plural='Tipos'

    def __str__ (self):
        return f"{self.TipoMarca}"