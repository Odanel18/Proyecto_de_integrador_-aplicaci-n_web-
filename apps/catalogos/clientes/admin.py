from django.contrib import admin

from apps.catalogos.clientes.models import Clientes

@admin.register(Clientes)
class ClienteAdmin(admin.ModelAdmin):
    search_fields = ['id', 'NumCedula']
    list_display = ['Nombres', 'Apellidos', 'NumCedula','NumTeléfono']
# Register your models here.
