from rest_framework.serializers import ModelSerializer
from .models import Marcas

class MarcaSerializer (ModelSerializer):
    class Meta:
        model=Marcas
        fields=['Nombre','TipoId']
