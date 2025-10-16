from django.contrib import admin
from apps.catalogos.moto.models import Moto

@admin.register(Moto)
class MotoAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['modelo', 'año','marcaId']
# Register your models here.
