from django.db import models

"""
Clientes
"""
class Cliente(models.Model):
    nombres = models.CharField(verbose_name='Nombre', max_length=100)
    apellidos = models.CharField(verbose_name="Apellidos", max_length=100)
    cedula = models.CharField(verbose_name='Número de cédula', max_length=16, unique=True)

    class Meta:
        verbose_name_plural = 'Clientes'
    
    def __str__(self):
        return f"{self.nombres} - {self.apellidos} - {self.cedula}"
    
    # comentario de prueba
    #
    #