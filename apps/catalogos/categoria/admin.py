from django.contrib import admin

from apps.catalogos.categoria.models import Categorias

@admin.register(Categorias)
class categoriaAdmin(admin.ModelAdmin):
    search_fields = ['id', 'Nombre']
    list_display = ['Nombre']
# Register your models here.
