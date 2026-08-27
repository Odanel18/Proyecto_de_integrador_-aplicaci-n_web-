from rest_framework.serializers import ModelSerializer, CharField
from rest_framework import serializers
from .models import Motos

class MotoSerializer (ModelSerializer):

    marca_nombre = serializers.CharField(source='MarcaId.Nombre', read_only=True)
    
    class Meta:
        model = Motos
        fields= ['id','Modelo','Año','MarcaId', 'marca_nombre']

        write_only_fields = ['MarcaId', 'id']