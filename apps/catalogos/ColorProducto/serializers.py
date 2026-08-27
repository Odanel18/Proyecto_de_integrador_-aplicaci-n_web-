from rest_framework.serializers import ModelSerializer
from .models import ColorProducto

class ColorProductoSerializer (ModelSerializer):
    class Meta:
        model=ColorProducto
        fields= ['id', 'Color']