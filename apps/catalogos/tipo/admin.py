from django.contrib import admin
from apps.catalogos.tipo.models import Tipo

@admin.register(Tipo)
class tipoAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['TipoMarca']
# Register your models here.
