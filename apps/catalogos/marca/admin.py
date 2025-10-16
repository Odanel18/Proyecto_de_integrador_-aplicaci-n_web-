from django.contrib import admin
from apps.catalogos.marca.models import Marca

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    search_fields = ['id', 'num_Factura']
    list_display = ['nombre', 'tipoId']
# Register your models here.