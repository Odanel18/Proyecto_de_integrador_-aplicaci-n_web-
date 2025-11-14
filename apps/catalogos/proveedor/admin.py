from django.contrib import admin
from apps.catalogos.proveedor.models import Proveedores

@admin.register(Proveedores)
class ProveedorAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['Nombre', 'Telefono']
# Register your models here.
