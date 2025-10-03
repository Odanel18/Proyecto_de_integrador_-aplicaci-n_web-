from django.contrib import admin

from apps.catalogos.clientes.models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    search_fields = ['id', 'cedula']
    list_display = ['nombres', 'apellidos', 'Num_cedula','Num_Telefono']
# Register your models here.
