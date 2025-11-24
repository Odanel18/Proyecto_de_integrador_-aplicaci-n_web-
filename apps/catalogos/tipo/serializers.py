from rest_framework.serializers import ModelSerializer
from .models import Tipo

class TipoSerializer (ModelSerializer):
    class Meta :
        model=Tipo
        fields=['TipoMarca']