from django.contrib import admin
from apps.catalogos.proveedor.models import Proveedor

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['nombre', 'telefono']
# Register your models here.
