from django.db import models

class EstadoCuenta (models.Model):
    descripcion = models.CharField (verbose_name="Descripcion", max_length= 50)
    estado= models.BooleanField(default=True)

    class Meta:
        verbose_name_plural:'EstadoCuenta'

    def __str__ (selt):
        return f'{selt.descripcion}'

