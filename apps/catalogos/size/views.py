from rest_framework.viewsets import ModelViewSet
from .models import Size
from .serializers import SizeSerializer

class SizeModelViewSet(ModelViewSet):
    queryset=Size.objects.filter(estado=True)
    serializer_class= SizeSerializer