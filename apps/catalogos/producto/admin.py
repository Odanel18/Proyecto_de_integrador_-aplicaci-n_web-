from django.contrib import admin
from apps.catalogos.producto.models import Productos

@admin.register(Productos)
class ProductoAdmin(admin.ModelAdmin):
    search_fields = ['id', 'Codigo']
    list_display = ['Codigo', 'Nombre','MarcaId','MotoId','CategoriaId','Stock','PrecioVenta']
# Register your models here.
