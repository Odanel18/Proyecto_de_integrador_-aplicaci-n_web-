from rest_framework.serializers import ModelSerializer, CharField
from .models import Marcas

class MarcaSerializer (ModelSerializer):

    tipo_nombre = CharField(source='TipoId.TipoMarca', read_only=True)

    class Meta:
        model=Marcas
        fields=['id','Nombre','TipoId', 'tipo_nombre']

        write_only_fields = ['TipoId', 'id']
