from rest_framework.serializers import ModelSerializer
from .models import Motos

class MotoSerializer (ModelSerializer):
    class Meta:
        model = Motos
        fields= ['Modelo','Año','MarcaId']