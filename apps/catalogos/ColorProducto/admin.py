from django.contrib import admin
from apps.catalogos.ColorProducto.models import ColorProducto
# Register your models here.

@admin.register(ColorProducto)
class ColorProductoAdmin(admin.ModelAdmin):
    search_fields = ['id', 'Color']
    list_display = ['Color']
