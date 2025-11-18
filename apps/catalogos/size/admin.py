from django.contrib import admin
from apps.catalogos.size.models import Size

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['descripcion']