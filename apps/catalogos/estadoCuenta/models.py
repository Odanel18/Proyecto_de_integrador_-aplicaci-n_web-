from django.db import models

class EstadoCuenta (models.Model):
    descripcion = models.CharField (verbose_name="Descripcion", max_length= 50)

    class Meta:
        verbose_name_plural:'EstadoCuenta'

    def __str__ (selt):
        return f'{selt.descripcion}'

