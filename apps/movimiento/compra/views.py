from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Compras,DetalleCompra
from .serializers import CompraSerializer,DetalleCompraSerializer

class CompraAPIView (APIView):
    def get(self,request):
        Serializer= CompraSerializer(Compras.objects.all(), many= True)
        return Response(status=status.HTTP_200_OK, data=Serializer.data)

class DetallecompraAPIView (APIView):
    def get(self,request):
        Serializer= DetalleCompraSerializer(DetalleCompra.objects.all(), many= True)
        return Response(status=status.HTTP_200_OK,data= Serializer.data)