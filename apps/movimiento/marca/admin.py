from django.contrib import admin
from apps.movimiento.marca.models import Marcas

@admin.register(Marcas)
class MarcaAdmin(admin.ModelAdmin):
    search_fields = ['id', ]
    list_display = ['Nombre', 'TipoId']
# Register your models here.