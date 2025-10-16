from django.contrib import admin

from apps.catalogos.categoria.models import Categoria

@admin.register(Categoria)
class categoriaAdmin(admin.ModelAdmin):
    search_fields = ['id', 'nombre']
    list_display = ['nombre']
# Register your models here.
