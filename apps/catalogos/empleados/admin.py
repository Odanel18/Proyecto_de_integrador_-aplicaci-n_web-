from django.contrib import admin
from apps.catalogos.empleados.models import Empleado

@admin.register(Empleado)
class EmpladoAdmin(admin.ModelAdmin):
    search_fields = ['id', 'num_Cedula']
    list_display = ['nombre', 'apellido','telefono','num_Cedula']
# Register your models here.